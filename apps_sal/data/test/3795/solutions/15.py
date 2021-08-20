n = int(input())
d = int(input())
e = int(input())
a = e * 5
m = 10000000
for i in range(min(100, n // a + 1)):
    if (n - a * i) % d < m:
        m = (n - a * i) % d
print(m)
