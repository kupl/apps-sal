a, b = list(map(int, input().split()))
if a == b:
    print(0)
else:
    a, b = max(a, b), min(a, b)
    x = a - b
    if a % x == 0 and b % x == 0:
        print(0)
    else:
        if a < 2 * b:
            print(x - b % x)
        else:
            lis = [i for i in range(1, int(x**0.5) + 1) if x % i == 0]
            for i in lis[::-1]:
                lis.append(x // i)
            import bisect
            y = bisect.bisect(lis, x // b)
            print(x // lis[y - 1] - b)
