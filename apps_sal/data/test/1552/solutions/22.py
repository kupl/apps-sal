n=int(input())
ar=list(map(int,input().split()))
k=min(ar.count(1),ar.count(2))
k=min(k,ar.count(3))
if k==0:
    print('0')
    return
z=[]
q=0
for x in range(n):
    if ar[x]==1:
        z.append([x+1])
        q+=1
    if q==k:
        break
q=0
for x in range(n):
    if ar[x]==2:
        z[q].append(x+1)
        q+=1
    if q==k:
        break
q=0
for x in range(n):
    if ar[x]==3:
        z[q].append(x+1)
        q+=1
    if q==k:
        break
print(k)
for x in z:
    print(' '.join(map(str,x)))

