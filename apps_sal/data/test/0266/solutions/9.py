m, s = map(int, input().split())
# for m in range(1, 100):
#    for s in range(1, 100):
# print(";;;;;;", s, m)
ar = [0] * m
ar[0] = 1
sum1 = 1
if m == 1:
    if s > 9:
        print('-1 -1')
    else:
        print(s, s)
else:
    dd = 0
    for i in range(m - 1, 0, -1):
        if sum1 <= s:
            ar[i] += 9
            sum1 += 9
        if sum1 > s:
            ar[i] -= sum1 - s
            sum1 -= sum1 - s
    if sum1 < s:
        ar[0] += s - sum1
    if ar[0] > 9:
        dd = 1
    min1 = ar[:]
    sum1 = 0
    ar = [0] * m
    ar[0] = 0
    for i in range(m):
        if sum1 <= s:
            sum1 += 9
            ar[i] += 9
        if sum1 > s:
            ar[i] -= sum1 - s
            sum1 -= sum1 - s
    if sum1 < s or dd == 1 or ar[0] == 0 or min(min1) < 0:
        print('-1 -1')
    else:
        print(''.join(map(str, min1)), ''.join(map(str, ar)))
