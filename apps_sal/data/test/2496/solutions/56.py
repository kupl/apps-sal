import math


def eratosthenes():
    erat = [0 for _ in range(max_a + 1)]
    pair = True
    for i in range(2, max_a + 1):
        cnt = 0
        if not erat[i]:
            for res in range(i, max_a + 1, i):
                if res in set_a:
                    cnt += 1
                erat[res] = i
                if cnt > 1:
                    pair = False
                    break
        if not pair:
            break
    return pair


n = int(input())
a = [int(x) for x in input().split()]
max_a = max(a)
set_a = set(a)
if eratosthenes() and len(set_a) == n - max(0, a.count(1) - 1):
    print('pairwise coprime')
else:
    res = a[0]
    for i in range(n):
        res = math.gcd(res, a[i])
    if res == 1:
        print('setwise coprime')
    else:
        print('not coprime')
