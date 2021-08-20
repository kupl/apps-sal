for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    if k > n:
        print(max(0, k - n))
    else:
        print((n - k) % 2)
