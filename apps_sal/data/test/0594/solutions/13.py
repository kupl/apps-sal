def R():
    return list(map(int, input().split()))


(n, m) = R()
a = R()
b = R()
v = max(2 * min(a), max(a))
print(v if v < min(b) else -1)
