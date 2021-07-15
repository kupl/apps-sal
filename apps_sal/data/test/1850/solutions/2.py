n,k = map(int,input().split())

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

imp = i = 0

while a[i]>a[k-1]+b[0]:
	imp += 1
	i += 1
key = a[k-1] + b[0]
a[k-1] += b[0]

for j in range(i):
	a[j] += b[j+1]

a = sorted(a, reverse=True)
	
ind = a.index(key)
q = imp+1

for k in range(n-1,ind,-1):
    a[k] += b[q]
    q += 1
    
a = sorted(a, reverse=True)
print(a.index(key)+1)
