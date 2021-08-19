n = int(input()) - 1
a = []
q = n // 26
r = n % 26
a.insert(0, r)
while q >= 26:
    q -= 1
    r = q % 26
    a.insert(0, r)
    q //= 26
a.insert(0, q - 1)
b = []
for i in range(len(a)):
    if a[i] >= 0:
        b.append(chr(a[i] + 97))
print(*b, sep='')
