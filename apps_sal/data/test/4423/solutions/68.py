l=int(input())
L=[]
for i in range(l):
    n,k=map(str,input().split())
    c=[]
    c.append(n)
    c.append(100-int(k))
    c.append(i+1)
    L.append(c)
L.sort()
for i in range(l):
    print(L[i][2])
