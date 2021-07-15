n=input().split()
r=int(n[0])
k=int(n[1])
l=[]
for i in range(r):
    li=input()
    l.append(li)
rl=[]
for i in range(r):
    x=[]
    for j in range(r):
        x.append(0)
    rl.append(x)
for i in range(r):
    for j in range(len(l[i])):
        flag=0
        f=0
        if j+k<=r:
            for q in range(k):
                if l[i][j+q:j+q+1]=='.':
                    continue
                else:
                    flag=1
                    break
            if flag==0:
                for q in range(k):
                    rl[i][j+q]=rl[i][j+q]+1
            if flag==1:
                j=q+1
for i in range(r):
    for j in range(r):
        flag=0
        f=0
        if j+k<=r:
            for q in range(k):
                if l[j+q][i:i+1]=='.':
                    continue
                else:
                    flag=1
                    break
            if flag==0:
                for q in range(k):
                    rl[j+q][i]=rl[j+q][i]+1
            if flag==1:
                j=q+1
maxi=0
maxj=0
m=0
for i in range(r):
    for j in range(r):
        if rl[i][j]>m:
            m=rl[i][j]
            maxi=i
            maxj=j
print(maxi+1,maxj+1)

