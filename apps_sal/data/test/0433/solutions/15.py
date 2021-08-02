n, a, b = list(map(int, input().split()))
if b == 0:
    print(a)
elif b < 0:
    k = abs(b)
    while k != 0:
        a -= 1
        if a == 0:
            a = n
        k -= 1
    print(a)
else:
    k = b
    while k != 0:
        a += 1
        if a > n:
            a = 1
        k -= 1
    print(a)
