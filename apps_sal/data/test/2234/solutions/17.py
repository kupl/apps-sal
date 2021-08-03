for _ in range(int(input())):
    n, k = [int(c) for c in input().split()]
    if k >= n:
        print(k - n)
    else:
        if (n + k) & 1:
            print(1)
        else:
            print(0)
