(n, k) = map(int, input().split())
print(sum(((n + 1 - i) * i + 1 for i in range(k, n + 2))) % (10 ** 9 + 7))
