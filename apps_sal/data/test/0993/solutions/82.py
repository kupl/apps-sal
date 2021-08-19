from collections import Counter
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
l = [0]
for i in range(N):
    l.append(A[i] + l[i])
for i in range(N + 1):
    l[i] %= M
c = Counter(l)
ans = 0
for i in c.values():
    ans += i * (i - 1) // 2
print(ans)
