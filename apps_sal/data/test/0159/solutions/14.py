def gcd(x, y):
    if x < y:
        t = x
        x = y
        y = t
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
b = [a[0]]
k = 0
for i in range(1, n):
    if gcd(a[i - 1], a[i]) != 1:
        b.append(1)
        k += 1
    b.append(a[i])
s = str(b[0])
for i in range(1, len(b)):
    s += ' ' + str(b[i])
print(k)
print(s)
