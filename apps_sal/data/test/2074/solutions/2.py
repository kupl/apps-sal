(n, m) = list(map(int, input().split()))
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
    b.append(min(a[i]))
print(max(b))
