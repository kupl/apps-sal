n,m,q = list(map(int,input().split()))
s = input()
t = input()
l = []
r = []
for i in range(n-m+1):
    if s[i:i+m] == t:
        l.append(i)
        r.append(i+m-1)
for i in range(q):
    x,y = list(map(int,input().split()))
    x-=1
    y-=1
    ans = 0
    for j in range(len(l)):
        if x <= l[j] and y >= r[j]:
            ans+=1
    print(ans)

