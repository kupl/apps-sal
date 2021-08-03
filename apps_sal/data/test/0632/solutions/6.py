for _ in range(int(input())):
    n, k = map(int, input().split())
    d1 = 2
    while n % d1 != 0:
        d1 += 1

    n = n + d1
    k -= 1
    n += k * 2
    print(n)
