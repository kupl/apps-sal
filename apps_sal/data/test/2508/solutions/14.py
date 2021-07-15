import sys
input = sys.stdin.readline
H,W,K = map(int,input().split())
r1,c1,r2,c2 = map(lambda x:int(x)-1,input().split())
C = [input() for i in range(H)]

def solve():
    from collections import deque
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    INF = float('inf')
    dists = [[INF]*W for _ in range(H)]
    dists[r1][c1] = 0
    q = deque([(r1,c1)])
    while q:
        y,x = q.popleft()
        if y==r2 and x==c2:
            print(dists[y][x])
            return
        for dx,dy in dxy:
            for i in range(1,K+1):
                nx,ny = x+dx*i,y+dy*i
                if not 0 <= nx < W: break
                if not 0 <= ny < H: break
                if C[ny][nx] == '@': break
                if dists[ny][nx] <= dists[y][x]: break
                if dists[ny][nx] <= dists[y][x] + 1: continue
                dists[ny][nx] = dists[y][x] + 1
                q.append((ny,nx))
    print(-1)
solve()
