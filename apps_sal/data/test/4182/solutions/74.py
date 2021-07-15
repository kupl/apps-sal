n,m,x,y = map(int,input().split())
xs = list(map(int,input().split()))
ys = list(map(int,input().split()))
xs.sort()
ys.sort()
if x >= y:
    print('War')
else:
    for i in range(x+1,y+1):
        if i > xs[-1] and i <= ys[0]:
            print('No War')
            return
        else:
            ans = 'War'
print(ans)
