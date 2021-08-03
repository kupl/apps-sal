n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if n >= m:
    print(0)
    return
b = []
for i in range(m - 1):
    b.append(a[i + 1] - a[i])

b.sort()
b = b[:m - n]
print(sum(b))
