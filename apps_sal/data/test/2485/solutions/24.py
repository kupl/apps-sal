H,W,M=list(map(int,input().split()))
row=[0]*H
col=[0]*W
target=set()
for i in range(M):
    h,w=list(map(int,input().split()))
    row[h-1]+=1
    col[w-1]+=1
    target.add((h-1,w-1))
A=max(row)
B=max(col)
a=[x for x in range(H) if row[x]==A]
b=[x for x in range(W) if col[x]==B]
for i in a:
    for j in b:
        if (i,j) not in target:
            print((A+B))
            return
print((A+B-1))

