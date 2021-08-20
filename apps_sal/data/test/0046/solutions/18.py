def d(a, b):
    return a // 5 * (b // 5)


(n, m) = map(int, input().split())
print(d(n, m) + d(n + 4, m + 1) + d(n + 3, m + 2) + d(n + 2, m + 3) + d(n + 1, m + 4))
