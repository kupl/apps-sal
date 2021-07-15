class Solution:
    
    def regionsBySlashes(self, grid: List[str]):
        def minAnglePoint(p1, p2, options):
            minAngle = 10.0     # a ridiculously big number
            for p3 in options:
                a = (p2[0] - p1[0], p2[1] - p1[1])
                b = (p3[0] - p2[0], p3[1] - p2[1])
                dot = a[0] * b[0] + a[1] * b[1]
                det = a[0] * b[1] - a[1] * b[0]
                ang = math.atan2(det, dot)
                if ang < minAngle: 
                    minAngle = ang
                    res = p3
            return res, minAngle

        N = len(grid)
        M = dict()
        for i in range(N):
            M[(i + 1, 0)] = [(i, 0)]
            M[(N, i + 1)] = [(N, i)]
            M[(N - i - 1, N)] = [(N - i, N)]
            M[(0, N - i - 1)] = [(0, N - i)]
        for y in range(N):
            x = 0
            for c in grid[y]:
                if c == '/':
                    if (x + 1, y) in M: 
                        M[(x + 1, y)].append((x, y + 1))
                    else: 
                        M[(x + 1, y)] = [(x, y + 1)]
                    if (x, y + 1) in M:
                        M[(x, y + 1)].append((x + 1, y))
                    else:
                        M[(x, y + 1)] = [(x + 1, y)]
                elif c == '\\\\':
                    if (x, y) in M: 
                        M[(x, y)].append((x + 1, y + 1))
                    else:
                        M[(x, y)] = [(x + 1, y + 1)]
                    if (x + 1, y + 1) in M: 
                        M[(x + 1, y + 1)].append((x, y))
                    else:
                        M[(x + 1, y + 1)] = [(x, y)]
                x += 1
        innerangle = round(-2 * math.pi, 4)
        points = sorted(M)
        regions = set()
        for i in range(len(points)):
            if points[i] not in M: continue
            startpoint = points[i]
            region = {startpoint}
            point = firststep = M[startpoint][0]
            M[startpoint].remove(point)
            prev = startpoint
            angSum = 0
            while point != startpoint:
                region.add(point)
                links = M[point]
                nxt, ang = minAnglePoint(prev, point, links)
                angSum += ang
                if len(links) == 1: 
                    del M[point]
                else:
                    M[point].remove(nxt)
                prev = point
                point = nxt
            if len(M[startpoint]) == 0: 
                del M[startpoint]
            
            _, ang = minAnglePoint(prev, point, [firststep])
            angSum = round(angSum + ang, 4)
            if angSum == innerangle: # it is a valid region
                regions.add(frozenset(region))
        return len(regions)
