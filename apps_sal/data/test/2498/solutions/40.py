import math
import sys
input = sys.stdin.readline
(N, M) = (int(x) for x in input().rstrip('\n').split())
As = [int(x) for x in input().rstrip('\n').split()]
n = 1
use2 = 0
check = 0
for i in range(N):
    x = As[i]
    if i == 0:
        while x % 2 == 0:
            use2 += 1
            x = x // 2
        lcm = x
    else:
        use = 0
        while x % 2 == 0:
            x = x // 2
            use += 1
        if use2 != use:
            check += 1
            break
        lcm = lcm * x // math.gcd(lcm, x)
if check > 0:
    print(0)
else:
    LCM = 2 ** (use2 - 1)
    LCM = LCM * lcm
    print((M // LCM + 1) // 2)
