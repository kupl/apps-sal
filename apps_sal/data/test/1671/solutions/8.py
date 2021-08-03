def inpList():
    return list(map(int, input().split()))


def inp():
    return int(input())


n = inp()
a = inpList()
x = sum(a)
p = x // n
t = x % n
a.sort()
suma = 0
for i in range(n - t):
    suma += abs(p - a[i])
for i in range(n - t, n):
    suma += abs(a[i] - p - 1)
print(suma // 2)
