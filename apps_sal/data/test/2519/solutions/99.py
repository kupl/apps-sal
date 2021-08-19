import copy
(n, k) = list(map(int, input().split()))
P = list(map(int, input().split()))
U = [0] * n
for i in range(n):
    U[i] = (P[i] + 1) / 2
ans = sum(U[:k])
t = copy.copy(ans)
for i in range(n - k):
    t = t + U[k + i] - U[i]
    ans = max(ans, t)
print(ans)
