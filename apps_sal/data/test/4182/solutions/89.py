n, m, x, y = map(int, input().split())
xlist = list(map(int, input().split()))
ylist = list(map(int, input().split()))
xlist.append(x)
ylist.append(y)
if max(xlist) < min(ylist):
    print('No War')
else:
    print('War')
