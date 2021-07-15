n = int(input())
a= list(map(int,input().split()))
bit = [0]*(n+1)
def update(idx,val):
    while idx<=n:
        bit[idx] = max(bit[idx],val)
        idx+=idx&(-idx)
def query(idx):
    res =0
    while idx>0:
        res = max(res,bit[idx])
        idx-=idx&(-idx)
    return res
b = []
for i in range(n):
    b.append([a[i],-(i+1)])
b.sort()
for i in range(n):
    qe = query(-b[i][1])
    update(-b[i][1],qe+1)
print(query(n))
