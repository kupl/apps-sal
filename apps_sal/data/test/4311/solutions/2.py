s = int(input())
a = s
c = 0
if a == 1 or a == 2:
    ans = 4
else:
    while a != 1:
        if a % 2 == 0:
            a = int(a / 2)
            c += 1
        else:
            a = int(3 * a + 1)
            c += 1
    ans = c + 2
print(ans)
