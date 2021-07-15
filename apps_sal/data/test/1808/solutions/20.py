n,k,x=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
a.reverse()
br=0
for i in range(n):
       if i+1<=k:
                   br=br+x
       else:
                   br=br+a[i]
print(br)
       

