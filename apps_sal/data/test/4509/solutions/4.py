for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    num = k // (n - 1)
    if k % (n - 1) == 0:
        ans = num * n - 1
    else:
        ans = num * n + k % (n - 1)
    print(ans)
