import sys
(N, K) = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = [(1 + p) / 2 for p in P]
temp = sum(Q[:K])
ans = temp
for i in range(N):
    try:
        temp = temp - Q[i] + Q[i + K]
        ans = max(ans, temp)
    except:
        pass
else:
    print(ans)
