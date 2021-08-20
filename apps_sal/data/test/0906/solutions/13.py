def pow(x, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return pow(x * x % mod, p // 2)
    return x * pow(x, p - 1) % mod


(n, m, k) = list(map(int, input().split()))
mod = 1000000007
if k == 1:
    if n == 1 or m == 1:
        print(1)
    else:
        print(pow(2, (n - 1) * (m - 1)))
elif n % 2 != m % 2:
    print(0)
elif n == 1 or m == 1:
    print(1)
else:
    print(pow(2, (n - 1) * (m - 1)))
