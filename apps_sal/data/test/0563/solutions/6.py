def gcd(a, b):
    rem = 0
    while b != 0:
        rem = a % b
        a = b
        b = rem
    return a


a, b = map(int, input().split())
if b - a == 1:
    print(-1)
else:
    found = False
    for i in range(a, b + 1):
        for j in range(i + 1, b + 1):
            for k in range(j + 1, b + 1):
                if gcd(i, j) == 1 and gcd(j, k) == 1 and gcd(i, k) != 1:
                    found = True
                    print(i, j, k)
                    break
            if found:
                break
        if found:
            break
    if not found:
        print(-1)
