bad = 0
n,x = map(int,input().split())
for i in range(n):
    c,d = input().split()
    d = int(d)
    if c=="+": x+=d
    else:
        if d>x:
            bad+=1
        else:
            x-=d
print(x,bad)
