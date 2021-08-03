import math
n, m = map(int, input().split())
aas = set(list(map(int, input().split())))
a = [i // 2 for i in aas]
N = len(a)


def n_of_twos(x):
    res = 0
    while x % (2**(res + 1)) == 0:
        res += 1
    return res


if N >= 2:
    n_of_twos_0 = n_of_twos(a[0])
    for i in range(1, N):
        if n_of_twos(a[i]) != n_of_twos_0:
            print(0)
            return
ans = a[0]
for i in range(1, N):
    ans = ans * a[i] // math.gcd(ans, a[i])
if ans > m:
    print(0)
    return
print(1 + (m // ans - 1) // 2)
