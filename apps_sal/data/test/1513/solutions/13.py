n, m, k = map(int, input().split())
b = list(map(int, input().split()))
l = n
p = n
c = []
for i in range(n - 1):
    c.append(b[i + 1] - b[i] - 1)
c = sorted(c)
for i in range(n - k):
    l += c[i]
print(l)
