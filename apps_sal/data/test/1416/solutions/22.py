n, w = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
v1 = a[0]
v2 = a[n]
q = min(v1, v2 / 2)
print(min(w, q * n * 3))
