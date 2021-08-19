for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    if k > n:
        print(k - n)
    elif (n - k) % 2 != 0:
        print(1)
    else:
        print(0)
