for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if n == k:
        print(0)
    elif n < k:
        print(k - n)
    else:
        if (n - k) % 2 == 0:
            print(0)
        else:
            print(1)
