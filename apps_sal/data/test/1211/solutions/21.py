(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = []
c = []
for x in a:
    b.append(n // x)
    c.append(n % x)
i = c.index(min(c))
print(i + 1, b[i])
