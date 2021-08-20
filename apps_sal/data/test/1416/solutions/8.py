(n, w) = map(int, input().split())
capac = list(sorted(map(int, input().split())))
boy = capac[len(capac) // 2]
girl = capac[0]
print(min(3 * girl * n, 3 / 2 * boy * n, w))
