n, m = list(map(int, input().split()))

if m % n > 0:
    print(-1)
else:
    res = 0
    a = m // n;
    while a % 2 == 0:
        a //= 2
        res += 1
    while a % 3 == 0:
        a //= 3
        res += 1
    if a == 1:
        print(res)
    else:
        print(-1)

