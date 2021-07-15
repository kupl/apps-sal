a=int(input())
l=list(map(int,input().split()))
r=list(map(int,input().split()))
e=r[0]
ans=[0]
for i in range(len(l)):
    if l[i]>=e:
        e=r[i]
        ans.append(i)
print(*ans)
