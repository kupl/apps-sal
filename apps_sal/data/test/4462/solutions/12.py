N = int(input())
ls = [int(s) for s in input().split()]
a0 = 0
a2 = 0
for n in ls:
    if n % 2 == 1:
        a0 += 1
    elif n % 4 == 0:
        a2 += 1
if a2 > a0 - 1:
    print('Yes')
elif a2 == a0 - 1:
    if a0 + a2 < N:
        print('No')
    else:
        print('Yes')
else:
    print('No')
