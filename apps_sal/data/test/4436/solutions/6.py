import sys
input = sys.stdin.readline


def factors(n):
    ret = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.add(i)
            ret.add(n // i)
    return ret


def solve(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and i != n // i:
            (a, b) = (i, n // i)
            (fa, fb) = (factors(a), factors(b))
            if len(fa) > 0:
                for fac in fa:
                    if len(set([fac, a // fac, b])) == 3:
                        return [fac, a // fac, b]
            if len(fb) > 0:
                for fac in fb:
                    if len(set([fac, b // fac, a])) == 3:
                        return [fac, b // fac, a]
    return 'NO'


for _ in range(int(input())):
    n = int(input())
    ans = solve(n)
    if ans == 'NO':
        print('NO')
    else:
        print('YES')
        print(*sorted(ans))
