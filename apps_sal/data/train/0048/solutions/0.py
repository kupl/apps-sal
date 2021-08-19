for haaghfj in range(int(input())):
    (x, y, k) = list(map(int, input().split()))
    print(k + (y * k + k - 1 + x - 2) // (x - 1))
