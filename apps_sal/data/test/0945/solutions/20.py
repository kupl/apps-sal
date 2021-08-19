def checkint(a, b, c, d):
    check = 0
    if min(a, b) < min(c, d) < max(a, b) < max(c, d) or min(c, d) < min(a, b) < max(c, d) < max(a, b):
        check = 1
    return check


n = int(input())
lis = input().split()
for i in range(n):
    lis[i] = int(lis[i])
intersect = 0
for i in range(n - 1):
    for j in range(n - 1):
        if checkint(lis[i], lis[i + 1], lis[j], lis[j + 1]) == 1:
            intersect = 1
if intersect == 0:
    print('no')
else:
    print('yes')
