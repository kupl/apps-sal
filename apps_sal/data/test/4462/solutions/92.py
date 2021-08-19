n = int(input())
a = list(map(int, input().split()))
li = [0, 0, 0]
for i in range(n):
    if a[i] % 4 == 0:
        li[2] += 1
        continue
    elif a[i] % 2 == 0:
        li[1] += 1
    else:
        li[0] += 1
if li[0] == 0:
    print('Yes')
elif li[0] == 1:
    if li[2] >= 1:
        print('Yes')
    else:
        print('No')
else:
    k = li[0]
    if n >= 2 * k:
        if li[2] >= k:
            print('Yes')
        else:
            print('No')
    elif n == 2 * k - 1:
        if li[2] >= k - 1:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
