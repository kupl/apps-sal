n, m = list(map(int, input().split()))
res = min(n, m // 2) + (m - min(n, m // 2) * 2) // 4
print(res)

