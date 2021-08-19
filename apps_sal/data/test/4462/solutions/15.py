n = int(input())
a = [int(x) for x in input().split()]
res = 'No'


def check(p):
    if p % 4 == 0:
        return 2
    elif p % 2 == 0:
        return 1
    else:
        return 0


c0 = 0
c2 = 0
c4 = 0
for i in range(n):
    a[i] = check(a[i])
    if a[i] == 2:
        c4 += 1
    elif a[i] == 1:
        c2 += 1
    else:
        c0 += 1
if c0 == c4 + 1 and c2 == 0:
    res = 'Yes'
elif c0 <= c4:
    res = 'Yes'
print(res)
