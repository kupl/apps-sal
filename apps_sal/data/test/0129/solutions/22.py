n, m, k, l = list(map(int, input().split()))

target = l + k
perfriend = target // m + (1 if target % m else 0)

if  perfriend * m > n or m > n or target > n:
    print(-1)
else:
    print(perfriend)


