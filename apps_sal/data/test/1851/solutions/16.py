n=int(input())
a=list(map(int, input().split()))
s=set()
ans=0
for i in range(len(a)):
    s.add(a[i]-1)
    if i in s:
        s.remove(i)
    if len(s)==0:
        ans+=1
print(ans)
    

