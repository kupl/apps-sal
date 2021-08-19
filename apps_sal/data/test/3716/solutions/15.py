from fractions import gcd
n = int(input())
lim = 50
r = 0
if n <= 2:
    print(n)
elif n == 3:
    print(6)
else:
    i = n
    while i > 0 and i > n - lim:
        j = i - 1
        while j > 0 and j > n - lim:
            k = j - 1
            while k > 0 and k > n - lim:
                x = i * j // gcd(i, j)
                x = k * x // gcd(k, x)
                r = max(r, x)
                k -= 1
            j -= 1
        i -= 1
    print(r)
