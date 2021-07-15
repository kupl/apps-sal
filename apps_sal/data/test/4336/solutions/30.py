W,H,x,y = map(int,input().split())

S = W * H * 0.5

if(x == W/2 and y == H/2):
    a = 1
else:
    a = 0

print(S,a)
