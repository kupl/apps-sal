n, k = map(int, input().split())
a = sorted(map(int, input().split()), reverse=True)
s = 0
need = 0
for i in range(n):
    if s + a[i] < k:
        s += a[i]
    else:
        need = i + 1
print(n - need)
