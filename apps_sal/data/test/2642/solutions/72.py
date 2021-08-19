from fractions import Fraction
from collections import defaultdict


def resolve():
    MOD = 1000000007
    N = int(input())
    zeroes = 0
    hash1 = defaultdict(int)
    hash2 = defaultdict(str)
    for _ in range(N):
        (a, b) = map(int, input().split())
        if a == 0 and b == 0:
            zeroes += 1
        elif b == 0:
            hash1['1/0'] += 1
            hash2['1/0'] = '0/1'
        elif a == 0:
            hash1['0/1'] += 1
            hash2['0/1'] = '1/0'
        else:
            rat1 = Fraction(a, b)
            rat2 = Fraction(-b, a)
            hash1[str(rat1)] += 1
            hash2[str(rat1)] = str(rat2)
    confirmed = set()
    ans = 1
    for (k, v) in hash1.items():
        if k in confirmed:
            continue
        bad = hash1.get(hash2[k], 0)
        cnt1 = pow(2, v, MOD) - 1
        cnt2 = pow(2, bad, MOD) - 1
        ans = ans * (cnt1 + cnt2 + 1) % MOD
        confirmed.add(k)
        confirmed.add(hash2[k])
    ans = (ans + zeroes + MOD - 1) % MOD
    print(ans)


def __starting_point():
    resolve()


__starting_point()
