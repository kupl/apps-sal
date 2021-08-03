n = int(input())
l1 = list(map(int, input().split()))
flag1 = 0
flag2 = 0
for item in l1:
    if item % 2 == 0:
        flag1 = 1
    else:
        flag2 = 1
if flag1 == 1 and flag2 == 1:
    l1.sort()
print(' '.join(str(x) for x in l1))
