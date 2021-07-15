n = int(input())
D = list(map(int, input().split()))
D.sort()

d = {}
c = 0
for i in range(n):
    d[D[i]] = d.get(D[i],0)+1
a1 = -1
a2 = -1
for i in d:
    c += d[i]
    if c==n//2:
        a1 = i
    if c>n//2:
        a2 = i
        break
if a1==-1 or a2==-1:
    print(0)
else:
    print(a2-a1)
