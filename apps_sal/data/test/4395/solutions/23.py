n=int(input())
s=list(input())
m=n//3
m+=1
a=list("GRB")
a=a*m
a=a[:n]
a1=list("GBR")
a1=a1*m
a1=a1[:n]
a2=list("RBG")
a2=a2*m
a2=a2[:n]
a3=list("RGB")
a3=a3*m
a3=a3[:n]
a4=list("BRG")
a4=a4*m
a4=a4[:n]
a5=list("BGR")
a5=a5*m
a5=a5[:n]
ans=[]
d=0
for i in range(n):
    if a[i]!=s[i]:
        d+=1
ans.append([d,0])
d=0
for i in range(n):
    if a1[i]!=s[i]:
        d+=1
ans.append([d,1])
d=0
for i in range(n):
    if a2[i]!=s[i]:
        d+=1
ans.append([d,2])
d=0
for i in range(n):
    if a3[i]!=s[i]:
        d+=1
ans.append([d,3])
d=0
for i in range(n):
    if a4[i]!=s[i]:
        d+=1
ans.append([d,4])
d=0
for i in range(n):
    if a5[i]!=s[i]:
        d+=1
ans.append([d,5])
ans.sort()
if ans[0][1]==0:
    print(ans[0][0])
    print(''.join(a))
elif ans[0][1]==1:
    print(ans[0][0])
    print(''.join(a1))
elif ans[0][1]==2:
    print(ans[0][0])
    print(''.join(a2))
elif ans[0][1]==3:
    print(ans[0][0])
    print(''.join(a3))
elif ans[0][1]==4:
    print(ans[0][0])
    print(''.join(a4))
elif ans[0][1]==5:
    print(ans[0][0])
    print(''.join(a5))

