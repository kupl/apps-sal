def kk():
    return map(int, input().split())


(n, m) = kk()
print(n - m if m * 2 > n else max(m, 1))
