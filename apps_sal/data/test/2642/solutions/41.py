
from collections import defaultdict
import math
import sys
readline = sys.stdin.readline

N = int(readline())

zeropair = 0
zeroa = 0
zerob = 0
pluspair = defaultdict(int)
minuspair = defaultdict(int)
for i in range(N):
    a, b = list(map(int, readline().split()))
    if a == 0 and b == 0:
        zeropair += 1
        continue
    if a == 0:
        zeroa += 1
        continue
    if b == 0:
        zerob += 1
        continue
    absa = abs(a)
    absb = abs(b)
    g = math.gcd(absa, absb)
    absa, absb = absa // g, absb // g
    if a * b > 0:
        pluspair[(absa, absb)] += 1
    else:
        minuspair[(absa, absb)] += 1

DIV = 1000000007
ans = 1
ans *= (pow(2, zeroa, DIV) + pow(2, zerob, DIV) - 1) % DIV
ans %= DIV

allcnt = 0

for item in list(pluspair.items()):
    a, b = item[0]
    cnt = item[1]
    if (b, a) in minuspair:
        ans *= (pow(2, cnt, DIV) + pow(2, minuspair[(b, a)]) - 1) % DIV
        ans %= DIV
        del minuspair[(b, a)]
    else:
        allcnt += cnt

for val in list(minuspair.values()):
    allcnt += val

ans = (ans * pow(2, allcnt, DIV)) % DIV
ans += zeropair
print(((ans - 1) % DIV))
