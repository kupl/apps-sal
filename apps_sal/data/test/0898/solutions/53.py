from math import sqrt
(N, M) = map(int, input().split())
cand = []
for i in range(1, int(sqrt(M)) + 1):
    if M % i == 0:
        cand.append(i)
        u = M // i
        if u != i:
            cand.append(u)
cand.sort()
ans = 1
for j in cand:
    if N * j <= M:
        ans = max(ans, j)
print(ans)
