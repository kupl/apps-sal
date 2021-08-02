n = int(input())
a = list(map(int, input().split()))
a.sort()
b = []
for i in range(n - 2):
    if not (a[i] == a[i + 1] and a[i] == a[i + 2]):
        b.append(a[i])
b.append(a[n - 2])
b.append(a[n - 1])
if b[-1] == b[-2]:
    b = b[:len(b) - 1]
print(len(b))
b1 = []
b2 = []
for i in range(len(b)):
    if i % 2 == 0:
        b2.append(b[i])
    else:
        b1.append(b[i])
for i in b1:
    print(i, end=' ')
b2.reverse()
for i in b2:
    print(i, end=' ')
