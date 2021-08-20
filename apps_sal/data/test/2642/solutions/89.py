import sys
from collections import defaultdict
from math import gcd
mod = 1000000007
N = int(input())


def reduce(vec):
    vec = list(vec)
    if vec[0] == 0:
        if vec[1] == 0:
            return (0, 0)
        else:
            return (0, 1)
    elif vec[1] == 0:
        return (1, 0)
    else:
        if vec[0] < 0:
            vec[0] = -vec[0]
            vec[1] = -vec[1]
        d = gcd(vec[0], vec[1])
        return (vec[0] // d, vec[1] // d)


counter0 = defaultdict(int)
counter1 = defaultdict(int)
origin = 0
for i in range(N):
    (a, b) = list(map(int, input().split()))
    if a == 0 and b == 0:
        origin += 1
        continue
    (a, b) = reduce((a, b))
    if b > 0:
        counter0[a, b] += 1
    else:
        counter0[-b, a] += 0
        counter1[-b, a] += 1
ans = origin
k = 1
for (key, cnt0) in list(counter0.items()):
    cnt1 = counter1[key]
    tmp = (pow(2, cnt0, mod) + pow(2, cnt1, mod) - 1) % mod
    k = k * tmp % mod
ans = ans + k - 1
ans %= mod
print(ans)
