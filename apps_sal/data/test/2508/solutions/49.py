from collections import deque

def main():
    H, W, K = list(map(int, input().split()))
    x1, y1, x2, y2 = list(map(int, input().split()))
    M = []
    Cost = [[1000000] * W for i in range(H)]
    dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    Cost[x1-1][y1-1] = 0
    q = deque([(x1-1, y1-1)])
    for h in range(H):
        M.append(list(input()))

    while q:
        x, y = q.popleft()
        for ddx, ddy in dxdy:
            for i in range(1, K+1):
                dx = ddx*i
                dy = ddy*i

                if not (0 <= x+dx < H and 0 <= y+dy < W):
                    break
                if M[x+dx][y+dy] == '@' or Cost[x+dx][y+dy] <= Cost[x][y]:
                    break
                if x+dx == x2-1 and y+dy == y2-1:
                    print((Cost[x][y]+1))
                    return
                if Cost[x+dx][y+dy] > Cost[x][y] + 1:
                    Cost[x+dx][y+dy] = Cost[x][y] + 1
                    q.append((x+dx,y+dy))
    

    print((-1))

    
def __starting_point():
    main()



__starting_point()
