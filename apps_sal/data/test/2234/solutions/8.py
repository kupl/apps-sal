for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if k > n:
        print(-n + k)
    else:
        if k % 2 != n % 2:
            print(1)
        else:
            print(0)

