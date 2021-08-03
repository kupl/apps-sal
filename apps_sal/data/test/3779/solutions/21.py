def gcd(a, b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(n):
    a[i] = a[i] % k
a.append(k)
b = 0
for i in range(n + 1):
    b = gcd(b, a[i])
c = []
for i in range(0, k, b):
    c.append(i)

print(len(c))
print(*c)
