(h, n) = map(int, input().split())
xlist = list(map(int, input().split()))
if sum(xlist) >= h:
    print('Yes')
else:
    print('No')
