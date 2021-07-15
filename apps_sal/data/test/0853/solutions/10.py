n = int(input())
a = list(map(int,input().split()))
c5 = 0
c0 = 0
for j in a:
    if j == 5:
        c5+=1
    else:
        c0+=1
if c5<9:
    if c0>0:
        print(0)
        return
    else:
        print(-1)
        return
else:
    if c0>0:
        print(int("5"*(c5-c5%9)+'0'*c0))
    else:
        print(-1)

