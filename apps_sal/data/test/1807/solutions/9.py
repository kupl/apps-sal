
def digit(i):
    if i == 0 or i == 6 or i == 9:
        return 6
    elif i == 1:
        return 2
    elif i == 2 or i == 3 or i == 5:
        return 5
    elif i == 4:
        return 4
    elif i == 7:
        return 3
    elif i == 8:
        return 7


def num(i):
    sum = 0
    for d in str(i):
        sum += digit(int(d))
    return sum


(a, b) = tuple(map(int, input().split()))

sum = 0
i = a
while i <= b:
    if i == 1 and b >= 100000:
        sum += 2383366
        i = 100001
    if i == 100001 and b >= 200000:
        sum += 2650003
        i = 200001
    if i == 200001 and b >= 300000:
        sum += 2950000
        i = 300001
    if i == 300001 and b >= 400000:
        sum += 2949999
        i = 400001
    if i == 400001 and b >= 500000:
        sum += 2850001
        i = 500001
    if i == 500001 and b >= 600000:
        sum += 2950001
        i = 600001
    if i == 600001 and b >= 700000:
        sum += 3049997
        i = 700001
    if i == 700001 and b >= 800000:
        sum += 2750004
        i = 800001
    if i == 800001 and b >= 900000:
        sum += 3149999
        i = 900001
    if i == 900001 and b >= 1000000:
        sum += 3050002
        i = 1000001
    if i <= b:
        sum += num(i)
        i += 1
    else:
        break

print(sum)
