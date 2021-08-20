for _ in range(int(input())):
    (n, r) = list(map(int, input().split()))
    x = min(n - 1, r)
    p = 0
    if r >= n:
        p = 1
    print(x * (x + 1) // 2 + p)
