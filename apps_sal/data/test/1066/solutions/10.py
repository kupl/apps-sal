(n, k) = [int(x) for x in input().strip().split()]
if k > (n + 1) // 2:
    k -= (n + 1) // 2
    print(2 * k)
else:
    print(2 * k - 1)
