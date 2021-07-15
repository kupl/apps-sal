n, m, k = [int(i) for i in input().split()]
n, m = min(n, m), max(n, m)
mod = 1000000007

def f_pow(a, k):
    if k == 0:
        return 1
    if k % 2 == 1:
        return f_pow(a, k - 1) * a % mod
    else:
        return f_pow(a * a % mod, k // 2) % mod

if k == -1:
    if (n % 2 == 0 and m % 2 == 1) or (n % 2 == 1 and m % 2 == 0):
        print(0)
    else:
        print(f_pow(2, (n - 1) * (m -1)) % mod)                               
else:
    print(f_pow(2, (n - 1) * (m -1)) % mod)

