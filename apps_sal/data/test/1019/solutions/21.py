def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


n = int(input())
m = 0
a = 0
b = 0
for i in range(1, n // 2 + 1):
    if nod(n - i, i) == 1:
        m = max(m, nod(n - i, i))
        (a, b) = (i, n - i)
print(a, b)
