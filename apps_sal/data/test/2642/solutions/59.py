from collections import defaultdict
import math
N = int(input())
m = defaultdict(lambda: 0)
BIG_NUMBER = 1000000007
bad_iwashi_count = 0
for _ in range(N):
    (A, B) = map(int, input().split())
    if A == 0 and B == 0:
        bad_iwashi_count += 1
        continue
    if A == 0:
        m[-1, 0, 1] += 1
        continue
    if B == 0:
        m[1, 1, 0] += 1
        continue
    gcd_ = math.gcd(A, B)
    A = A // gcd_
    B = B // gcd_
    if A < 0 and B > 0:
        m[-1, -A, B] += 1
    elif B < 0 and A > 0:
        m[-1, A, -B] += 1
    elif A < 0 and B < 0:
        m[1, -A, -B] += 1
    elif A > 0 and B > 0:
        m[1, A, B] += 1
total = 1
for key in list(dict(m).keys()):
    total *= pow(2, m[key], BIG_NUMBER) + pow(2, m[-key[0], key[2], key[1]], BIG_NUMBER) - 1
    total %= BIG_NUMBER
    m.pop(key)
    m.pop((-key[0], key[2], key[1]))
print((total + bad_iwashi_count - 1) % BIG_NUMBER)
'\n3\n1 2\n-1 1\n2 -1\n'
