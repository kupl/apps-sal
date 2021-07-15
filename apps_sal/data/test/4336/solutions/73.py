W,H,x,y = map(int,input().split())
if x == W/2 and y == H/2:
    ans = 1
else:
    ans = 0
print(W*H/2,ans)
