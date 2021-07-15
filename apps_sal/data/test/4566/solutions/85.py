n,m = map(int,input().split())
s = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    s[a-1].append(b)
    s[b-1].append(a)
for i in s:
    print(len(i))
