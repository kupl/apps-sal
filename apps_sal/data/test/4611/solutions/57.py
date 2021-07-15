n = int(input())
pt, px, py = 0,0,0
f = 0
for i in range(n):
    t,x,y = map(int, input().split())
    gt = t-pt
    gx, gy = abs(x-px), abs(y-py)
    gt -= gx+gy
    if gt < 0 or gt%2==1:
        f=1
    pt,px,py = t,x,y
if f:
    print("No")
else:
    print("Yes")
