n, m = map(int, input().split())

if m % n != 0:
    print(-1)
else:
    x = m // n
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    while x % 3 == 0:
        x //= 3
        k += 1
    if x == 1:
        print(k)
    else:
        print(-1)
