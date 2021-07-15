n,k=(int(i)for i in input().split())
a=[int(i) for i in input().split()]
b=[int(i)for  i in input().split()]
t=[[a[i],b[i]]for i in range(n)]
t.sort(key=lambda x:[x[0],-x[1]])
now=t[0][0]
time=[]
chosen=1
for i in range(1,n):
    if t[i][0]!=now:
        chosen+=1
        now=t[i][0]
    else:
        time.append(t[i][1])
time.sort()
print(sum(time[:(k-chosen)]))

