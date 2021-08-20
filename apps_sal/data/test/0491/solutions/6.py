n = int(input())
if n >= 0:
    print(n)
else:
    n = -n
    a = n % 10
    n //= 10
    b = n % 10
    n //= 10
    n = n * 10 + min(a, b)
    print(-n)
