l=int(input())
n=len(bin(l-1))-2 #頂点数
V=[]
if all([(l-1)>>i&1 for i in range(n)]):
    n+=1
    for i in range(n-1):
        V.append([i+1,i+2,0])
        V.append([i+1,i+2,2**(n-i-2)])


else:
    for i in range(n-1):
        V.append([i+1,i+2,0])
        V.append([i+1,i+2,2**(n-i-2)])

    now=2**(n-1)
    for i in range(n-2):
        if (l-1)>>(n-i-2)&1:
            V.append([1,i+2,now])
            now+=2**(n-i-2)
    if (l-1)&1:
        V.append([1,n-1,now])
    else:
        V.append([1,n,now])
print(n,len(V))
for v in V:
    print(*v)
