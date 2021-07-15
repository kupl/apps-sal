n=input()
digs=[]
edigs=[]
for i in range(len(n)):
    digs.append(int(n[i]))
    if int(n[i])%2==0:
        edigs.append([int(n[i]),i])
if len(edigs) is 0:
    print(-1)
else:
    cool=len(edigs)
    for i in range(len(edigs)):
        if edigs[i][0]<digs[-1]:
            cool=min(cool,i)
    if cool == len(edigs):
        digs[edigs[-1][1]]=digs[-1]
        digs[-1]=edigs[-1][0]
    else:
        digs[edigs[cool][1]]=digs[-1]
        digs[-1]=edigs[cool][0]
    ans=''
    for element in digs:
        ans+=str(element)
    print(ans)
