n = int(input())
if n % 2:
    a = [i for i in range(n)]
    b = [i for i in range(n)]
    c = [(a[i] + b[i]) % n for i in range(n)]
    print(*a)
    print(*b)
    print(*c)
else:
    print(-1)
