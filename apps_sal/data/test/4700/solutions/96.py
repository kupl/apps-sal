_,H,*P=open(0);*H,=map(int,[0]+H.split());T=[1]*len(H)
for p in P:
 a,b=map(int,p.split());T[min(a,b,key=lambda x:H[x])]=0
 if H[a]==H[b]:T[b]=0
print(sum(T)-1)
