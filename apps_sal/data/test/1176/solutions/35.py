n=int(input())
a=list(map(int,input().split()))
c=0#負数の数
ab=10**10#絶対値の最小
s=0#絶対値の総和
for i in range(n):
    if a[i]<0:
        c+=1
    if ab>abs(a[i]):
        ab=abs(a[i])
    s+=abs(a[i])
if c%2==0:
    print(s)
else:
    print((s-2*ab))

