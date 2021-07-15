def bin_pow(n, s):
    if s == 0:
        return 1
    else:
        if s % 2 == 0:
            t = bin_pow(n, s / 2) % 998244353
            return (t * t) % 998244353
        else:
            return ((bin_pow(n, s - 1) % 998244353) * n) % 998244353
tr, tl = list(map(int, input().split()))
a = input()
b = input()

ans = 0
ansd = 0
for i in range(tl):
    if tr - i - 1 > -1 and a[tr - i - 1] == "1":
        ansd += bin_pow(2, i)
        ansd %= 998244353
    if b[tl - i - 1] == "1":
        ans += ansd
        ans %= 998244353
print(ans % 998244353)

