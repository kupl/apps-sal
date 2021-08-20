import collections
(N, K) = map(int, input().split())
L = list(map(int, input().split()))
L = sorted(L)
c = collections.Counter(L)
c = c.most_common()
ans = 0
if len(c) > K:
    for i in range(len(c) - K):
        ans += c[len(c) - i - 1][1]
    print(ans)
else:
    print(0)
