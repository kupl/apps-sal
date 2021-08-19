from collections import Counter
(N, M) = map(int, input().split())
A = list(map(int, input().split()))


def nC2(n):
    return n * (n - 1) // 2


cum = [A[0] % M]
for i in range(1, N):
    cum.append((cum[-1] + A[i]) % M)
c = Counter(cum)
ans = c[0]
for k in c.keys():
    ans += nC2(c[k])
print(ans)
