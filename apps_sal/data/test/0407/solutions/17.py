mat=[]
for i in range(10):
    l=[0 for i in range(10)]
    mat.append(l)
    l=[]
verif=[True for i in range(10)]
find=[False for i in range(10)]
s=[]
n=int(input())
for i in range(n):
    p=input()
    for j in range(len(p)):
        g=6-len(p)
        mat[ord(p[j])-97][g+j]+=1
        find[ord(p[j])-97]=True
    verif[ord(p[0])-97]=False
for i  in range(10):
    if(find[i]==True):
        u=0
        for j in range(6):
            u=u+mat[i][j]*(10**(5-j))
        s.append((u,i,verif[i]))
s=sorted(s)
s=s[::-1]
pos=0
for i in range(len(s)):
    if(verif[s[i][1]]==True):
        pos=i
        break
somme=0
k=1
r=True
for i in range(len(s)):
    if((s[i][2]==True)and(r==True)):
        r=False
    else:
        somme=somme+k*s[i][0]
        k=k+1
print(somme)
