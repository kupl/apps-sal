n = int(input())
a = list(map(int, input().split()))
b = 0
for i in range(n):
    b += a[i]
c = int(b / n)
d = c + 1
e = 0
f = 0
for i in range(n):
    e += (a[i] - c) ** 2
    f += (a[i] - d) ** 2
print(min(e, f))
