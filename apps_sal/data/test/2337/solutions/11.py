def R():
    return list(map(int, input().split()))


(n, m) = R()
a = R()
b = R()
c = 0
i = j = 0
while i < n:
    while j < m and b[j] < a[i]:
        j += 1
    if j == m:
        break
    c += 1
    i += 1
    j += 1
print(n - c)
