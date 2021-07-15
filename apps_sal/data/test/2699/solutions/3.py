t=0
try:
    t=int(input())
except:
    pass
for _ in range (t):
    try:
        l=list(map(int,input().split()))
    except:
        pass
for n in l:
    if n in range (1,31):
        a,b,c,d=1,2,4,3
        print("1",end=' ')
        for _ in range (n-1):
            a=(a+1)*2
            print(a,end=' ')
        print("")
        print("2",end=' ')
        for _ in range (n-1):
            b=(b*2)+1
            print(b,end=' ')
        print("")
        print("4",end=' ')
        for _ in range (n-1):
            c=(c*2)+2
            print(c,end=' ')
        print("")
        print("3",end=' ')
        for _ in range (n-1):
            d=d*2
            print(d,end=' ')
        print("")
