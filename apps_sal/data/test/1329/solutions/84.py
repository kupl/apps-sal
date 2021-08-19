from collections import defaultdict
from functools import reduce
from operator import mul
N = int(input())


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, list(range(n, n - r, -1)))
    under = reduce(mul, list(range(1, r + 1)))
    return over // under


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


count = 1
D = defaultdict(int)
for i in range(1, N + 1):
    f = factorization(i)
    for t in f:
        (num, con) = t
        D[num] += con
threes = 0
fives = 0
num_15 = 0
num_25 = 0
num_75 = 0
for v in list(D.values()):
    if v >= 2:
        threes += 1
    if v >= 4:
        fives += 1
    if v >= 14:
        num_15 += 1
    if v >= 24:
        num_25 += 1
    if v >= 74:
        num_75 += 1
ans = (threes - fives) * fives * (fives - 1) // 2
if fives >= 3:
    ans += fives * (fives - 1) * (fives - 2) // 2
ans += num_75
ans += num_15 * (fives - 1)
ans += num_25 * (threes - 1)
print(ans)
