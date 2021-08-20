def R():
    return map(int, input().split())


(n, m) = R()
a = list(R())
b = list(R())
a.sort(reverse=True)
b.sort(reverse=True)
a1 = a[0] * b[0]
a2 = a[0] * b[m - 1]
a3 = a[n - 1] * b[0]
a4 = a[n - 1] * b[m - 1]
if max(a1, a2, a3, a4) == max(a1, a2):
    a = a[1:]
else:
    a = a[:n - 1]
a1 = a[0] * b[0]
a2 = a[0] * b[m - 1]
a3 = a[n - 2] * b[0]
a4 = a[n - 2] * b[m - 1]
print(max(a1, a2, a3, a4))
