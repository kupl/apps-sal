import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0 for _ in range(N + 1)]
for i in range(len(A)):
    S[i + 1] = (S[i] + A[i]) % M

c = collections.Counter(S)
ans = 0
for val in c.values():
    ans += (val * (val - 1)) // 2
print(ans)
