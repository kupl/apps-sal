def solve():
    (n, m) = list(map(int, input().split()))
    i = 0
    while n != 0:
        i += 1
        n -= 1
        if i % m == 0:
            n += 1
    print(i)


solve()
