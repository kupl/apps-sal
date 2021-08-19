n = int(input())
a = list(map(int, input().split()))
one = 0
four = 0
two = 0
for i in range(n):
    cnt = 0
    num = a[i]
    while num % 2 == 0:
        cnt += 1
        num //= 2
    if cnt == 0:
        pin = 1
    elif cnt == 1:
        pin = 2
    else:
        pin = 4
    if pin == 1:
        one += 1
    elif pin == 4:
        four += 1
    else:
        two += 1
if two > 0:
    one += 1
if one <= four + 1:
    print('Yes')
else:
    print('No')
