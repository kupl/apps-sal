for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if k >= n:
        print(k - n)
    else:
        if n % 2 != k % 2:
            print(1)
        else:
            print(0)

