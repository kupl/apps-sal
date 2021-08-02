import sys
input = sys.stdin.readline
n = int(input())

mod = 998244353
now = n * pow(2, n - 1, mod)
k = pow(2, n, mod)
k = pow(k, mod - 2, mod)
if n == 1:
    print(now * k % mod)
elif n == 2:
    print(now * k % mod)
    print(now * k % mod)
elif n == 3:
    print(now * k % mod)
    print(now * k % mod)
    print(now * k % mod)
else:
    ans = []
    ans.append(now * k % mod)
    ans.append(now * k % mod)
    for i in range(2, n // 2):
        now += (2 * i - 1) * pow(2, (2 * i - 3), mod)
        ans.append(now * k % mod)
    sna = list(reversed(ans))
    if n % 2 == 1:
        i = n // 2
        now += (2 * i - 1) * pow(2, (2 * i - 3), mod)
        ans.append(now * k % mod)
    print(*(ans + sna), sep="\n")
