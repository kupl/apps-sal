n  =int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))

l = []

for i in range(n):
    l.append(v[i]-c[i])


ans = 0
for i in l:
    if i>0:
        ans+=i
print(ans)

