L = list(map(int, input().split()))
for i in range(2**4):
    a = 0
    b = 0
    for j in range(4):
        if (i >> j) & 1:
            a += L[j]
        else:
            b += L[j]
    if a == b:
        print('Yes')
        return
else:
    print('No')
