n, p, k = map(int, input().split())
a = []
for i in range(p-k, p+k+1):
    a.append(i)
while a[0]<1:
    a.pop(0)
while a[len(a)-1]>n:
    a.pop()
if a[0]!=1:
    print("<<",end=" ")
for i in a:
    v = i
    if v==p:
        v = '('+str(v)+')'
    print(v, end=" ")
if a[len(a)-1]!=n:
    print(">>")

