from bisect import bisect_left,bisect
a,b,q = map(int,input().split())
jin = [-10**16]
for i in range(a):
    jin.append(int(input()))
jin.append(10**16)
tera = [-10**20]
for i in range(b):
    tera.append(int(input()))
tera.append(10**20)
for i in range(q):
    x = int(input())
    j = bisect(jin,x)
    t = bisect(tera,x)
    j1 = jin[j]
    j2 = jin[j-1]
    t1 = tera[t]
    t2 = tera[t-1]
    ans = min(abs(x-j1)+abs(j1-t1),abs(x-j1)+abs(j1-t2),abs(x-j2)+abs(j2-t1),abs(x-j2)+abs(j2-t2))
    ans = min(ans,abs(x-t1)+abs(t1-j1),abs(x-t1)+abs(t1-j2),abs(x-t2)+abs(t2-j1),abs(x-t2)+abs(t2-j2))
    print(ans)
