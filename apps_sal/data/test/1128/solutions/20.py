lis = input().split()
a = int(lis[0])
m = int(lis[1])
if m % 2 == 1:
    if a % m == 0:
        print('Yes')
    else:
        print('No')
else:
    k = 0
    while 2 ** k <= m and m % 2 ** k == 0:
        k += 1
    k -= 1
    u = m // 2 ** k
    if a % m % u == 0:
        print('Yes')
    else:
        print('No')
