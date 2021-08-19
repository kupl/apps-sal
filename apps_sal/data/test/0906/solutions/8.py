def bin_exp(x, n, m):
    r = 1
    while n > 0:
        if n % 2 == 1:
            r = r * x % m
        x = x * x % m
        n = n // 2
    return r


M = 1000000007
I = [int(i) for i in input().split()]
n = I[0]
m = I[1]
k = I[2]
if n % 2 != m % 2 and k == -1:
    print(0)
else:
    h = bin_exp(2, n - 1, M)
    h = bin_exp(h, m - 1, M)
    print(h)
