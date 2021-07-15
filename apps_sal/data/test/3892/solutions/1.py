from collections import defaultdict as dd, deque

n,m = list(map(int,input().split()))

S = dd(list)

for _ in range(m):
    start,dest = list(map(int,input().split()))
    S[start-1].append(dest-1)

closest = [0]*n
for i in range(n):
    if S[i]:
        closest[i] = min((j-i)%n for j in S[i])

R = [0]*n
for start in range(n):
    mx = 0
    for di in range(n):
        i = (start + di)%n
        cost = di + (len(S[i])-1)*n + closest[i]
        mx = max(mx, cost)
    R[start] = mx

print(' '.join([str(x) for x in R]))




