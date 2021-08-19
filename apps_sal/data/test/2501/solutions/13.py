import collections
N = int(input())
A = list(map(int, input().split()))
plus = [0] * N
minus = [0] * N
for i in range(N):
    plus[i] = i + 1 + A[i]
    minus[i] = i + 1 - A[i]
plus = dict(collections.Counter(plus))
minus = dict(collections.Counter(minus))
ans = 0
for i in list(plus.keys()):
    if i in minus:
        ans += plus[i] * minus[i]
print(ans)
