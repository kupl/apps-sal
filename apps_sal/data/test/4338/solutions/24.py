n,x,y = list(map(int, input().split()))
m = list(map(int, input().split()))
if(x>y):
    print(n)
else:
    s = 0
    for i in range(n):
        if(m[i]<=x):
            s+=1
    print((s+1)//2)

