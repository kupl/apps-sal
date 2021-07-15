# F - XOR Matching
from collections import deque

m, k = map(int, input().split())

# k>=2^mの時は成立しない
if k>=pow(2,m):
    print(-1)

# m=0の時
elif m==0:
    print(0, 0)

# m=1の時
elif m==1:
    if k==0:
        print(0, 0, 1, 1)
    else:
        print(-1)

# m>=2の時
else:
    ans = deque()
    ans.append(k)
    for i in range(pow(2,m)):
        if i!=k:
            ans.append(i)
            ans.appendleft(i)
    ans.append(k)
    print(' '.join(map(str, ans)))
