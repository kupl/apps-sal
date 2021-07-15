n=int(input())
s=list(input())
a=[0]*3
for l in s:
    a[int(l)]+=1
ans=[None]*n
i=0
for l in s:
    if int(l)==1 and a[0]<n//3<a[1]:
       ans[i]='0'
       a[0]+=1
       a[1]-=1
    elif  int(l)==2 and a[0]<n//3<a[2]:
        ans[i] = '0'
        a[0] += 1
        a[2] -= 1
    elif  int(l)==2 and a[1]<n//3<a[2]:
        ans[i] = '1'
        a[1] += 1
        a[2] -= 1
    else:
        ans[i]=l
    i+=1
i=n-1
for l in ans[::-1]:
    if int(l)==0 and a[2]<n//3<a[0]:
        ans[i] = '2'
        a[2] += 1
        a[0] -= 1
    elif int(l)==1 and a[2]<n//3<a[1]:
        ans[i] = '2'
        a[2] += 1
        a[1] -= 1
    elif int(l)==0 and a[1]<n//3<a[0]:
        ans[i] = '1'
        a[1] += 1
        a[0] -= 1
    i-=1
print(''.join(ans))
