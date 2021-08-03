def leap(k): return (k % 4 == 0 and k % 100 != 0) or k % 400 == 0


y = int(input())
if leap(y):
    flag = True
else:
    flag = False
d = 7
x = y
d2, flag2 = d, flag
while 1:
    x += 1
    d2 -= 1
    if leap(x):
        d2 -= 1
        flag2 = True
    else:
        flag2 = False
    if d2 <= 0:
        d2 += 7
    if (d2, flag2) == (d, flag):
        break
print(x)
