from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))
idx = defaultdict(int)

for i in range(N):
    idx[a[i]] = i
    
m = min(a)
M = max(a)
ans = []

if abs(M)>abs(m):
    for i in range(N):
        ans.append((idx[M], i))
    
    for i in range(1, N):
        ans.append((i-1, i))
else:
    for i in range(N):
        ans.append((idx[m], i))
    
    for i in range(N-2, -1, -1):
        ans.append((i+1, i))

print((len(ans)))

for x, y in ans:
    print((x+1, y+1))

