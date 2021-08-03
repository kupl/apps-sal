n = int(input())
s = input().split()
m = [-1]
ch = 1
md = 1000000007
for i in range(n):
    m.append(int(s[i]))
    ch = (ch * int(s[i])) % md
m.sort()
kol = 1
z = 1
kolraz = 0
fl = 1
sq = 1
for i in range(2, n + 1):
    if m[i] == m[i - 1]:
        kol += 1
    else:
        for j in range(kol // 2):
            sq = (sq * m[i - 1]) % md
        if kol % 2 == 1:
            fl = 0
        z *= (kol + 1)
        kol = 1
        kolraz += 1
z *= (kol + 1)
for j in range(kol // 2):
    sq = (sq * m[n]) % md
if kol % 2 == 1:
    fl = 0
res = 1
kol = z
kol //= 2
if fl:
    res = sq
while kol:
    if kol & 1:
        res = (res * ch) % 1000000007
    ch = (ch * ch) % md
    kol >>= 1
print(res)
