A,B=map(int,input().split())
for i in range(1500):
    if(i*2//25==A and i//10==B):
        print(i)
        return
else:
    print(-1)
