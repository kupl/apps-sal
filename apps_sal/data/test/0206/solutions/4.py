import sys
import math
input = sys.stdin.readline


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


(m, a, b) = list(map(int, input().split()))
GCD = gcd(a, b)
MODLIST = [-1] * a
NOWMAX = a
NOW = a
MODLIST[0] = a
while True:
    while NOW - b > 0 and MODLIST[(NOW - b) % a] == -1:
        NOW -= b
        MODLIST[NOW] = NOWMAX
    NOW += a
    NOWMAX = max(NOW, NOWMAX)
    if MODLIST[(NOW - b) % a] != -1:
        break
ANS = m + 1
MAX = max(MODLIST)
for i in range(1, min(m + 1, MAX)):
    if MODLIST[i % a] == -1:
        continue
    ANS += max(m + 1 - max(MODLIST[i % a], i), 0)
if MAX <= m:
    ANS += (m - MAX + 1 + (m - m // GCD * GCD) + 1) * ((m // GCD * GCD - MAX) // GCD + 1) // 2
print(ANS)
