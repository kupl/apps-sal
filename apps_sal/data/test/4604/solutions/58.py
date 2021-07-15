from typing import Counter


n = int(input())
lis = list(map(int, input().split()))
mod  =10**9+7

ans = 0
if n % 2 == 0:
    b = Counter(lis)
    flag = 1
    for i in list(b.values()):
        if i == 2:
            pass
        else:
            flag = 0
            break
    if flag:
        ans = 2**(n//2)
        print((ans % mod))
    else:
        print((0))
else:
    lis = sorted(lis)
    lis = lis[1:]
    b = Counter(lis)
    flag = 1
    for i in list(b.values()):
        if i == 2:
            pass
        else:
            flag = 0
            break
    if flag:
        ans = 2**(n//2)
        print((ans % mod))
    else:
        print((0))

