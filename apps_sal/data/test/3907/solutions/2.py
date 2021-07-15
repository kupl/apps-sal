def Fun(n):
    if(n%2): return n*(n-1)//2+1
    return n*n//2

n,m = list(map(int,input().split()))
q = [0] * (m)
w = [0] * (m)
for i in range(m):
    q[i],w[i] = [int(x) for x in input().split()]
    #print(q[i],w[i])
w.sort(reverse = True)
#print(*w)
s = 0
v = 0
#print("n=",n)
for i in range(m):
    #print("i=",i," v=",v,"w[i]=",w[i])
    if(Fun(i+1)>n): break
    s+=w[i]
print(s)

