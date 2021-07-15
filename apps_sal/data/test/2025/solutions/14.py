n=int(input())
m=[]
for i in range(n):
    m.append(int(input()))
for i in m:
    if (i%2==0):
        if (i>=4):
            print(i//4)
        else:
            print(-1)
    else:
        if (i==9) or (i>=13):
            print((i-9)//4+1)
        else:
            print(-1)
