def mp():
    return map(int, input().split())


(n, l, r) = mp()
min_s = n - l + 2 ** l - 1
max_s = (n - r) * 2 ** (r - 1) + 2 ** r - 1
print(min_s, max_s)
