import sys
input = sys.stdin.readline
H,W,N = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(N)]
from collections import defaultdict
dic = defaultdict(lambda: 0)
for y,x in AB:
    for dx in range(-1,2):
        for dy in range(-1,2):
            nx,ny = x+dx,y+dy
            if not 1 <= nx <= W: continue
            if not 1 <= ny <= H: continue
            dic[(nx,ny)] += 1

ans = [0] * 10
for (x,y),c in dic.items():
    if x==1 or x==W or y==1 or y==H: continue
    ans[c] += 1
s = sum(ans)
ans[0] = (W-2)*(H-2)-s

print(*ans, sep='\n')
