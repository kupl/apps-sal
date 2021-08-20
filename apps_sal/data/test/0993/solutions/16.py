from itertools import accumulate
from collections import Counter
(N, M) = map(int, input().split())
As = list(map(int, input().split()))


def f(a, b):
    return (a + b) % M


cumsum = list(accumulate([0] + As, f))
answer = 0
for (k, v) in Counter(cumsum).items():
    answer += v * (v - 1) // 2
print(answer)
