from math import gcd
MOD = 10 ** 9 + 7
N = int(input())
d = {}
zero = 0
for _ in range(N):
    (a, b) = list(map(int, input().split()))
    if a == b == 0:
        zero += 1
        continue
    if b < 0:
        b = -b
        a = -a
    g = gcd(a, b)
    b //= g
    a //= g
    if b == 0 and a == -1:
        a = 1
    if a > 0:
        if (a, b) in d:
            d[a, b][0] += 1
        else:
            d[a, b] = [1, 0]
    elif (b, -a) in d:
        d[b, -a][1] += 1
    else:
        d[b, -a] = [0, 1]
ans = 1
for ((a, b), (k, l)) in list(d.items()):
    ans *= pow(2, k, MOD) - 1 + pow(2, l, MOD) - 1 + 1
    ans %= MOD
ans -= 1
ans += zero
ans %= MOD
print(ans)
