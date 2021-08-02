n = int(input())

s = input()

sum1 = 0
kol1 = 0
sum2 = 0
kol2 = 0

for i in range(n // 2):
    if s[i] == '?':
        kol1 += 1
    else:
        sum1 += int(s[i])

for i in range(n // 2, n):
    if s[i] == '?':
        kol2 += 1
    else:
        sum2 += int(s[i])

if sum1 > sum2:
    sum1, sum2, kol1, kol2 = sum2, sum1, kol2, kol1


if sum1 == sum2 and kol1 == kol2:
    print('Bicarp')
elif sum1 == sum2 and kol1 != kol2:
    print('Monocarp')
elif (sum2 - sum1) % 9 != 0:
    print('Monocarp')
elif kol1 == kol2 == 0:
    print('Monocarp')
elif (sum2 - sum1) // 9 == (kol1 - kol2) // 2:
    print('Bicarp')
else:
    print('Monocarp')
