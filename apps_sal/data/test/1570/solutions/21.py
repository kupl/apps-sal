n, k, m = [int(x) for x in input().split()]
s = ((n + m * n) * m) // 2
print(max(0, s - k))
