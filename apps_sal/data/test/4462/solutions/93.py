# 2 2 4 1 4 1
# 1 4 1 2 2
n = int(input())
a = list(map(int,input().split()))
i2 = 0
i4 = 0
for i in range(n):
    if a[i]%4==0:
        i4 += 1
    if a[i]%2==0:
        i2 += 1

if n//2 <= i4:
    print('Yes')
else:
    tmp = n//2
    if n%2==0:
        if (tmp - i4) * 2 <= (i2 - i4):
            print('Yes')
        else:
            print('No')
    else:
        if (tmp - i4) * 2 + 1 <= (i2 - i4):
            print('Yes')
        else:
            print('No')

