(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
a1 = 0
a2 = 2 * n
a4 = n
flag = True
s1 = 0
s2 = 0
for x in a:
    while x >= 3:
        if a4:
            a4 -= 1
            x -= 4
        elif a2 > 1:
            a2 -= 1
            x -= 2
        else:
            flag = False
            break
    if not flag:
        break
    if x == 2:
        s2 += 1
    elif x == 1:
        s1 += 1
while s2:
    if a2:
        a2 -= 1
        s2 -= 1
    elif a4:
        a4 -= 1
        a1 += 1
        s2 -= 1
    else:
        s1 += 2
        s2 -= 1
print('YES' if flag and a1 + a2 + a4 * 2 >= s1 else 'NO')
