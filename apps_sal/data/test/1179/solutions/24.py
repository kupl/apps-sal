n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list()
c = 1
d = w = 0
for i in range(100000):
    b.append(c)
    if c == k:
        w = i
        break
    elif c > k:
        w = i - 1
        break
    d += 1
    c += d
print(a[k - b[w]])
