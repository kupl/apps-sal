n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
b = [0]
c = n
d = 1
for i in range(n - 1):
    if a[i] == a[i + 1]:
        d += 1
        c -= 1
    else:
        b.append(d)
        d = 1
b.append(d)
b.sort()
for i in range(len(b) - 1):
    b[i + 1] += b[i]
print((b[max(0, c - k)]))
