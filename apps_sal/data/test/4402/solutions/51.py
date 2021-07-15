a,b=list(map(int ,input().split()))
if(a>=13):
    print(int(b))
elif(a>=6 and a<=12):
    print(int(b/2))
elif(a==5 or a<5):
    print(0)
