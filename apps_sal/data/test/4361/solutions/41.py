n,k=map(int,input().split())
h=[int(input()) for i in range(n)]

h.sort()

l=[]
for i in range(n-k+1):
        a=h[i+k-1]-h[i]
        l.append(a)

print(min(l))
