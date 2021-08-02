a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
acount = 0
bcount = 0
ccount = 0

x, y = input().split()

for i in range(0, 7):
    if int(x) == a[i] or int(y) == a[i]:
        acount += 1

for i in range(0, 4):
    if int(x) == b[i] or int(y) == b[i]:
        bcount += 1

if int(x) == c[0]:
    ccount += 1
if int(y) == c[0]:
    ccount += 1


if acount == 2 or bcount == 2 or ccount == 2:
    print("Yes")
else:
    print("No")
