a = int(input())
aa = a
c = 0
if (a % 400 == 0 or (a % 100 != 0 and a % 4 == 0)):
    c = 366
else:
    c = 365
a += 1
while c % 7 != 0 or (a % 400 == 0 or (a % 100 != 0 and a % 4 == 0)) != (aa % 400 == 0 or (aa % 100 != 0 and aa % 4 == 0)):
    if (a % 400 == 0 or (a % 100 != 0 and a % 4 == 0)):
        c += 366
    else:
        c += 365
    a += 1
print(a)
