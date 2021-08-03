a, b = input().split()
a = int(a)
b = int(b)
c = list(map(int, input().split()))
m = a * b
for i in range(a - 1):
    if c[i + 1] - c[i] < b:
        m = m - (b - (c[i + 1] - c[i]))
print(m)
