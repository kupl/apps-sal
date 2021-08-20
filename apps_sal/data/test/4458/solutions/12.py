import sys
N = int(input())
P = list(map(int, input().split()))
m = 100000000000000
cnt = 0
for i in range(N):
    if P[i] <= m:
        cnt += 1
    m = min(m, P[i])
print(cnt)
