for _ in range(int(input())):
    (x, y, k) = [int(s) for s in input().split()]
    n = ((y + 1) * k - 1 + (x - 2)) // (x - 1)
    print(n + k)
