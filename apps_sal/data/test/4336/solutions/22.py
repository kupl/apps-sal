W,H,x,y = map(int,input().split())
flag = 0
if x ==  W/2 and y ==  H/2:
    flag = 1
print(W*H/2,flag)    
