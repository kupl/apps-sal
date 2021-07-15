import sys
from collections import deque
input = sys.stdin.readline

def main():
    h, w, k = list(map(int, input().split()))
    sx, sy, gx, gy = list(map(int, input().split()))

    c = [input() for i in range(h)]

    not_yet = deque([(sx-1, sy-1)])
    dist = [[-1]*w for i in range(h)]
    dist[sx-1][sy-1] = 0
    already = [[False]*w for i in range(h)]
    already[sx-1][sy-1] = True

    while not_yet:
        x, y = not_yet.popleft()
        d = dist[x][y]

        for i in range(x+1, x+k+1):
            if i >= h or c[i][y] == "@":
                break
            if already[i][y] and dist[i][y] < d + 1:
                break
            if already[i][y] and dist[i][y] == d + 1:
                continue
            dist[i][y] = d + 1
            already[i][y] = True
            not_yet.append((i, y))

        for i in range(x-1, x-k-1, -1):
            if i < 0 or c[i][y] == "@":
                break
            if already[i][y] and dist[i][y] < d + 1:
                break
            if already[i][y] and dist[i][y] == d + 1:
                continue
            dist[i][y] = d + 1
            already[i][y] = True
            not_yet.append((i, y))
        
        for i in range(y+1, y+k+1):
            if i >= w or c[x][i] == "@":
                break
            if already[x][i] and dist[x][i] < d + 1:
                break
            if already[x][i] and dist[x][i] == d + 1:
                continue
            dist[x][i] = d + 1
            already[x][i] = True
            not_yet.append((x, i))

        for i in range(y-1, y-k-1, -1):
            if i < 0 or c[x][i] == "@":
                break
            if already[x][i] and dist[x][i] < d + 1:
                break
            if already[x][i] and dist[x][i] == d + 1:
                continue
            dist[x][i] = d + 1
            already[x][i] = True
            not_yet.append((x, i))

    ans = dist[gx-1][gy-1]
    print(ans)

    
def __starting_point():
    main()


__starting_point()
