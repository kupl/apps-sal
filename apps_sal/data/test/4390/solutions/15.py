for i in range(int(input())):
    n, m = list(map(int, input().split()))
    ch = n % m
    if ch == 0:
        ch = m
    print(m - ch)
