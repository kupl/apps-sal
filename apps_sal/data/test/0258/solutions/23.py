#585_D

n = int(input())

ln = list(input())

sm1 = 0
sm2 = 0
qs1 = 0
qs2 = 0

for i in range(0, n // 2):
    if ln[i] != "?":
        qs1 += 1
        sm1 += int(ln[i])
    if ln[n // 2 + i] != "?":
        qs2 += 1
        sm2 += int(ln[n // 2 + i])

qs1 = n // 2 - qs1
qs2 = n // 2 - qs2
qs = qs1 + qs2

m = False

if not qs:
    if sm1 != sm2:
        m = True

mx = sm1 + min(qs1, qs // 2) * 9
lft = min(qs2, qs2 - ((qs // 2) - qs1))
if mx > lft * 9 + sm2:
    m = True

mx = sm2 + min(qs2, qs // 2) * 9
lft = min(qs1, qs1 - ((qs // 2) - qs2))
if mx > lft * 9 + sm1:
    m = True

if m:
    print("Monocarp")
else:
    print("Bicarp")

