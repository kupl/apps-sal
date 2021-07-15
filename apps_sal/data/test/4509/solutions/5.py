for t in range(int(input())):
    n, k = list(map(int, input().split()))
    if k % (n - 1) == 0:
        print(k // (n - 1) * n - 1)
    else:
        print(k // (n - 1) * n + k % (n - 1))
