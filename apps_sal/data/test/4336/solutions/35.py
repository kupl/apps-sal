W,H,x,y = map(int,input().split())
ans1 = (W*H)/2
if (x == W/2) and (y == H/2):
    ans2 = 1
else:
    ans2 = 0
print(ans1,ans2)
