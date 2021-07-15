n,m,a,b = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.sort()
y.sort()
if x[-1]<y[0]:
    for i in range(x[-1]+1,y[0]+1):
        if a<i<b:
            print("No War")
            break
    else:
        print("War")
else:
    print("War")
