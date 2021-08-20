class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        q = collections.deque([source])
        visited = set([tuple(source)])
        blocked = set([tuple(b) for b in blocked])
        lb = len(blocked) * 3
        r = math.ceil(lb / math.pi / 2.0)
        Max = math.ceil(r * r * math.pi)
        (dx, dy) = ([0, 1, 0, -1], [1, 0, -1, 0])
        breakflag = False
        while q:
            if len(visited) > Max:
                breakflag = True
                break
            l = len(q)
            for i in range(l):
                (x, y) = q.popleft()
                for j in range(4):
                    (newx, newy) = (x + dx[j], y + dy[j])
                    if 0 <= newx < 1000000 and 0 <= newy < 1000000 and ((newx, newy) not in visited) and ((newx, newy) not in blocked):
                        if newx == target[0] and newy == target[1]:
                            return True
                        visited.add((newx, newy))
                        q.append((newx, newy))
        if breakflag == False:
            return False
        breakflag = False
        q = collections.deque([target])
        visited = set([tuple(target)])
        while q:
            if len(visited) > Max:
                breakflag = True
                break
            l = len(q)
            for i in range(l):
                (x, y) = q.popleft()
                for j in range(4):
                    (newx, newy) = (x + dx[j], y + dy[j])
                    if 0 <= newx < 1000000 and 0 <= newy < 1000000 and ((newx, newy) not in visited) and ((newx, newy) not in blocked):
                        visited.add((newx, newy))
                        q.append((newx, newy))
        if breakflag == False:
            return False
        return True
