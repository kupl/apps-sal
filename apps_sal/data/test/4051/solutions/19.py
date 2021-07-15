n=int(input())
a=list(map(int,input().split()))
s=set()
for i in range(n-1):
    s.add(abs(a[i]-a[i+1]))
if len(list([x for x in s if x>1]))>0:print('NO')
else:print('YES')

