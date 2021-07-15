def gcd(a, b):
    while a>0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

n = int(input())
for i in range(n // 2, 0, -1):
    if gcd(i, n - i) == 1:
        print(i, n - i)
        break
