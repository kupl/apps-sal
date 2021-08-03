n = int(input())
if n & 1:
    print(n // 2)
else:
    k = 1
    while k <= n:
        k *= 2
    print((n - k // 2) // 2)
