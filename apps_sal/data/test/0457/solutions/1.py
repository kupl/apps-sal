import math
import sys
input = sys.stdin.readline
(x, n) = list(map(int, input().split()))
mod = 10 ** 9 + 7
L = int(math.sqrt(x))
FACT = dict()
for i in range(2, L + 2):
    while x % i == 0:
        FACT[i] = FACT.get(i, 0) + 1
        x = x // i
if x != 1:
    FACT[x] = FACT.get(x, 0) + 1
ANS = 1
for f in FACT:
    for k in range(1, 70):
        t = n // f ** k
        if t == 0:
            break
        ANS = ANS * pow(f, t, mod) % mod
print(ANS)
