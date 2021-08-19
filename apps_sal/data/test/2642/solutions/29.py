import sys
from math import gcd
from collections import Counter
read = sys.stdin.read
readline = sys.stdin.readline
(N, *AB) = list(map(int, read().split()))
mod = 10 ** 9 + 7
ab = []
zero = 0
for (A, B) in zip(*[iter(AB)] * 2):
    if A == 0 and B == 0:
        zero += 1
        continue
    if A == 0:
        B = -1
    elif B == 0:
        A = 1
    else:
        g = gcd(A, B)
        A //= g
        B //= g
    if A < 0:
        (A, B) = (-A, -B)
    ab.append((A, B))
cnt = Counter(ab)
answer = 1
checked = set()
ok = 0
for ((i, j), n) in list(cnt.items()):
    if (i, j) in checked:
        continue
    if j < 0:
        (c, d) = (-j, i)
    else:
        (c, d) = (j, -i)
    if (c, d) in cnt:
        m = cnt[c, d]
        answer = answer * (pow(2, n, mod) + pow(2, m, mod) - 1) % mod
        checked.add((c, d))
    else:
        ok += n
answer *= pow(2, ok, mod)
answer -= 1
answer += zero
answer %= mod
print(answer)
