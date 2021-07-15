n = int(input())
l1 = []
l2 = []
for i in range(n):
    a,b = list(map(int,input().split()))
    l1.append(a)
    l2.append(b)
l1.sort()
l2.sort()
ans = 0
kk = 0
c = 0
cc = 0
i = 0
while i<n:
    if l1[i]<l2[cc]:
        c+=1
        if c>ans:
            kk = l1[i]
            ans = c
        i+=1
    else:
        cc+=1
        c-=1
    
print(kk,ans)
    

