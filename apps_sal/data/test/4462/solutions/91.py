N = int(input())
a = [int(i) for i in input().split()]
ki = 0
gu_2 = 0
gu_4 = 0
for i in a:
    if i % 4 == 0:
        gu_4 += 1
    elif i % 2 == 0:
        gu_2 += 1
    else:
        ki += 1
if ki <= gu_4:
    print('Yes')
elif gu_4 + 1 == ki and gu_4 + ki == N:
    print('Yes')
else:
    print('No')
