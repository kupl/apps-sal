e = 0
s = 0
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    s += a[i]
    if i % 2 == 1:
        e += a[i]

b = []
for i in range(n):
    if (i == 0):
        b.append(s - 2 * e)
    else:
        b.append(2 * a[i - 1] - b[i - 1])

print(" ".join(map(str, b)))
