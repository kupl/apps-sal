n,x= map(int,input().split())
tp=0
for i in range(n):
    ct = (2**(n-i+2)-4)//2+1
    if x==0:break
    if i==n-1:tp+='bpppb'[:x].count('p')
    else:
        pn = 2**(n-i)-1
        if x<ct:x-=1
        elif x>=ct:
            tp+=pn+1
            if x==ct:break
            x-=ct
print(tp)
