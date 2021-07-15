t=int(input())
pre=[]
curr=[]
for i in range(t):
    s1=input()
    pre.append(s1)
for i in range(t):
    s2=input()
    curr.append(s2)
z=0
for i in range(t):
    if pre[i] in curr:
        curr.remove(pre[i])
        pass
    else:
        z+=1
print(z)
