N,M,X,Y = list(map(int,input().split()))
x=max(list(map(int,input().split())))
y=min(list(map(int,input().split())))

for z in range(X+1,Y+1):
    if x<z<=y:
        print("No War")
        return
print("War")

