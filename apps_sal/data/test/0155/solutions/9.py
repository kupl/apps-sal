n, m, k = list(map(int, input().split()))
if k < n:
    print(k + 1, 1)
elif (k - n) // (m - 1) % 2 == 0:
    print(n - (k - n) // (m - 1), (k - n) % (m - 1) + 2)
else:
    print(n - (k - n) // (m - 1), m - (k - n) % (m - 1))
