a,b=map(int,input().split())
for i in range(1,10**5):
    c = a*i
    if c%b==0:
        print(c)
        return
