import math
from collections import defaultdict
N = int(input())
dic = defaultdict(int)
mod = 1000000007
for _ in range(N):
    (A, B) = list(map(int, input().split()))
    if A < 0:
        (A, B) = (-A, -B)
    if A == 0:
        if B == 0:
            dic[0, 0] += 1
        else:
            dic[0, -1] += 1
    elif B == 0:
        dic[1, 0] += 1
    else:
        gcd = math.gcd(A, B)
        (A, B) = (A // gcd, B // gcd)
        dic[A, B] += 1
ans = 1
N -= dic[0, 0]
for (k, v) in list(dic.items()):
    if k == (0, 0):
        continue
    (a, b) = k
    if not (b, -a) in dic:
        continue
    v_dash = dic[b, -a]
    ans *= pow(2, v, mod) - 1 + (pow(2, v_dash, mod) - 1) + 1
    ans %= mod
    N -= v + v_dash
ans *= pow(2, N, mod)
ans += dic[0, 0] - 1
ans %= mod
print(ans)
