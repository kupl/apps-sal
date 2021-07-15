n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
cb=[]
for i in range(m):
    b, c = list(map(int, input().split()))
    cb.append([c,b])
cb.sort(reverse=True)
k=0
for i in range(m):
    j=0
    while j<cb[i][1] and k+j<n and a[k+j]<cb[i][0]:
        a[k+j] = cb[i][0]
        j+=1
    k+=j
    if k==n:
        break
print((sum(a)))

