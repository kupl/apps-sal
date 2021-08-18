a = list(map(int, input().split()))
c = 0
for i in range(2):
    c += a[a.index(max(a))]
    a[a.index(max(a))] = a[a.index(max(a))] - 1

print(c)
