N=int(input())
A=['3','5','7']
i=0
while 1:
    now=A[i]
    if int(now+'3')<=N:A.append(now+'3')
    if int(now+'5')<=N:A.append(now+'5')
    if int(now+'7')<=N:A.append(now+'7')
    else:break
    i+=1

ans=0
B={'3','5','7'}
for a in A:
    if set(list(a))&B==B:
        ans+=1
print(ans)
