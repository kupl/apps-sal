import math
(d, g) = list(map(int, input().split()))
prob = []
for i in range(d):
    (p, c) = list(map(int, input().split()))
    prob.append([p, c, p * (i + 1) * 100 + c])
mindays = 10 ** 9
for i in range(2 ** d):
    point = 0
    days = 0
    one = []
    for j in range(d):
        if i >> j & 1 == 0:
            point += prob[j][2]
            days += prob[j][0]
        else:
            one.append(j + 1)
    if point >= g:
        mindays = min(mindays, days)
    elif point < g:
        for k in range(len(one)):
            day = days
            tmp = math.ceil((g - point) / (one[k] * 100))
            if tmp <= prob[one[-1] - 1][0]:
                day += tmp
                mindays = min(mindays, day)
print(mindays)
