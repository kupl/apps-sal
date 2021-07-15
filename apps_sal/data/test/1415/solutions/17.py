x, y, sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1

direction = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}

visited = [[False] * y for i in range(x)]
prev = sx, sy

s = input()
sm = x * y - 1

print (1, end = ' ')
visited[prev[0]][prev[1]] = True

for c in s[:-1]:
    d = direction[c]
    cur = tuple(map(sum, zip(prev, d)))
    if not 0 <= cur[0] < x or not 0 <= cur[1] < y:
        cur = prev
    p = 1 - visited[cur[0]][cur[1]]
    print (p, end = ' ')
    sm -= p
    visited[cur[0]][cur[1]] = True
    prev = cur

print (sm)



