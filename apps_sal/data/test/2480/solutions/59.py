import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0]
for a in A:
    b = (B[-1] + (a-1)) % K
    B.append(b)

ans = 0
dic = {}
for i, b in enumerate(B):
    if b in dic:
        dic[b].append(i)
    else:
        dic[b] = deque()
        dic[b].append(i)
    
    while len(dic[b]) > 0 and dic[b][0] <= i - K:
        dic[b].popleft()
    ans += len(dic[b])-1
    

print(ans)
