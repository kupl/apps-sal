n, k = [int(x) for x in input().split()]

if k <= (n + 1) // 2:
    print(2 * (k - 1) + 1)
else:
    k -= (n + 1) // 2
    print(2 * k)

