n = int(input())

o = n // 2 + n % 2
e = n // 2

kk = [0] * (e + e + o)

r = 0
for i in range(e):
    kk[r] = 2 + i * 2
    r += 1

for i in range(o):
    kk[r] = 1 + i * 2
    r += 1

for i in range(e):
    kk[r] = 2 + i * 2
    r += 1


print(len(kk))
print(' '.join(map(str, kk)))
