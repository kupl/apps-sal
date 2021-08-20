(a, b) = sorted(list(map(int, input().split())))
if a == b:
    print(0)
elif a > b - a:
    if a % (b - a) == 0:
        print(0)
    else:
        print(b - a - a % (b - a))
elif (b - a) % a == 0:
    print(0)
else:
    ans = float('inf')
    for q in range(1, int((b - a) ** (1 / 2)) + 2):
        if (b - a) % q == 0:
            if (b - a) // q >= a:
                ans = min(ans, (b - a) // q)
            if q >= a:
                ans = min(ans, q)
    print(ans - a)
