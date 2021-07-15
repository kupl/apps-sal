a,b,c,x,y=list(map(int,input().split()))


moneys=[]
for i in range(0,max(x,y)*2+1,2):
    apizza=x-int(i/2)
    bpizza=y-int(i/2)
    if apizza<0:
        apizza=0
    if bpizza<0:
        bpizza=0
    money=apizza*a+bpizza*b+i*c
    moneys.append(money)

print((min(moneys)))

