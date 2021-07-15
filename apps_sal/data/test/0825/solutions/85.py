N=int(input());P=[];Q=[];a=0
for i in range(2,10**3):
 if all(i%p for p in P):P.append(i)
for i in range(3,10**6):
 if all(i%p for p in P):Q.append(i)
for p in P+Q:
 i=0
 while N%p<1:N//=p;i+=1
 a+=int((2*i+.25)**.5-.5)
print(a+(N>1))
