n = int(input())
a = [int(x) for x in input().split()]
D = {}
for x in a:
    if x in D:
        D[x] += 1
    else:
        D[x] = 1
maxans = 0


def check(x, y):
    num = 2
    D[x] -= 1
    D[y] -= 1
    while x + y in D and D[x + y] > 0:
        D[x + y] -= 1
        x, y = y, x + y
        num += 1
    ans = num
    while num > 2:
        D[y] += 1
        x, y = y - x, x
        num -= 1
    D[x] += 1
    D[y] += 1
    return ans


for x in D:
    for y in D:
        if x == y and D[x] == 1:
            continue
        maxans = max(check(x, y), maxans)

print(maxans)
