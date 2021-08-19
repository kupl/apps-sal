(n, k) = [int(x) for x in input().split()]
if k == 1:
    print(1)
elif k == 2:
    print(int(n * (n - 1) / 2 + 1))
elif k == 3:
    print(int(n * (n - 1) * (n - 2) / 3 + n * (n - 1) / 2 + 1))
elif k == 4:
    print(int(3 * n * (n - 1) * (n - 2) * (n - 3) / 8 + n * (n - 1) * (n - 2) / 3 + n * (n - 1) / 2 + 1))
