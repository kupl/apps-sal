INF = 1e11

move = {'W': (0, 1), 'A': (-1, 0), 'S': (0, -1), 'D': (1, 0)}


def getExtremes(positions):
    minX, minY, maxX, maxY = [positions[0][0]], [positions[0][1]], [positions[0][0]], [positions[0][1]]
    for p in positions[1:]:
        minX.append(min(minX[-1], p[0]))
        minY.append(min(minY[-1], p[1]))
        maxX.append(max(maxX[-1], p[0]))
        maxY.append(max(maxY[-1], p[1]))
    return minX, minY, maxX, maxY


t = int(input())

while t > 0:
    t -= 1
    s = input()
    x, y = 0, 0
    positions = [(0, 0)]
    for c in s:
        x, y = x + move[c][0], y + move[c][1]
        positions.append((x, y))
    minXBeg, minYBeg, maxXBeg, maxYBeg = getExtremes(positions)
    positions.reverse()
    minXEnd, minYEnd, maxXEnd, maxYEnd = getExtremes(positions)
    minXEnd.reverse()
    minYEnd.reverse()
    maxXEnd.reverse()
    maxYEnd.reverse()
    positions.reverse()
    ans = INF
    for i in range(len(s)):
        for c in move:
            minX = min(minXBeg[i], positions[i][0] + move[c][0], minXEnd[i + 1] + move[c][0])
            maxX = max(maxXBeg[i], positions[i][0] + move[c][0], maxXEnd[i + 1] + move[c][0])
            minY = min(minYBeg[i], positions[i][1] + move[c][1], minYEnd[i + 1] + move[c][1])
            maxY = max(maxYBeg[i], positions[i][1] + move[c][1], maxYEnd[i + 1] + move[c][1])
            area = (maxX - minX + 1) * (maxY - minY + 1)
            ans = min(ans, area)
    print(ans)
