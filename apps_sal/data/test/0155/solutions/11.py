(n, m, k) = list(map(int, input().split()))
if k < n:
    print(1 + k, 1)
else:
    k -= n
    k2 = k // (m - 1)
    k3 = k % (m - 1)
    if k2 % 2 == 0:
        print(n - k2, k % (m - 1) + 2)
    else:
        print(n - k2, m - k % (m - 1))
