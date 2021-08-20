from itertools import accumulate
from math import floor, sqrt
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
sm = sum(A)
divs = set()
for i in range(1, floor(sqrt(sm)) + 1):
    if sm % i == 0:
        divs.add(i)
        divs.add(sm // i)
ans = 1
for d in divs:
    ls = sorted(map(lambda x: x % d, A))
    acc = [0] + list(accumulate(ls, lambda x, y: x + y))
    for i in range(1, N):
        minus = acc[i] - acc[0]
        plus = d * (N - i) - (acc[-1] - acc[i])
        if plus == minus and plus <= K:
            ans = max(ans, d)
print(ans)
