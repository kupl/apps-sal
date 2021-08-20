(H, N) = map(int, input().split())
Alist = list(map(int, input().split()))
if H > sum(Alist):
    print('No')
else:
    print('Yes')
