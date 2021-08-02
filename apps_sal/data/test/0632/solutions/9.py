for f in range(int(input())):
    n, k = map(int, input().split())
    div = 2
    while div * div < n and n % div != 0:
        div += 1
    if div * div > n:
        div = n
    print(n + div + (k - 1) * 2)
