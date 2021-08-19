(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
s2 = n * 2
s4 = n
s1 = 0
f = 1
rem1 = 0
rem2 = 0
for i in range(len(a)):
    if f:
        while a[i] >= 3:
            if s4 > 0:
                a[i] -= 4
                s4 -= 1
            elif s2 > 0:
                a[i] -= 2
                s2 -= 1
            else:
                f = 0
        if a[i] == 1 and f:
            rem1 += 1
        elif a[i] == 2 and f:
            rem2 += 1
while rem2 > 0 and f:
    if s2 > 0:
        rem2 -= 1
        s2 -= 1
    elif s4 > 0:
        rem2 -= 1
        s4 -= 1
        s1 += 1
    else:
        rem2 -= 1
        rem1 += 2
if rem1 > s1 + s2 + s4 * 2:
    f = 0
if f:
    print('YES')
else:
    print('NO')
