a = str(input())
b = str(input())
n = len(a)
unos = [0] * (n + 1)
m = len(b)
tot = 0
for el in b:
    tot += int(el)
tot = tot % 2
s = 0
c = 0
for r in range(1, n + 1):
    s += int(a[r - 1])
    unos[r] = s
    if r >= m and (unos[r] - unos[r - m]) % 2 == tot:
        c += 1
print(c)
