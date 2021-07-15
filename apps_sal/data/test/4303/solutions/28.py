n,k = map(int, input().split())
lst = list(map(int, input().split()))

ne_lst = []
po_lst = []
for i in lst:
    if i < 0:
        ne_lst.append(-i)
    else:
        po_lst.append(i)
ne_lst.reverse()

res = 10**10
if len(ne_lst) >= k:
    res = min(res, ne_lst[k-1])
if len(po_lst) >= k:
    res = min(res, po_lst[k-1])
for i, j in enumerate(ne_lst):
    if  k-(i+1)>0 and len(po_lst) > (k-1)-(i+1):
        res = min(res, ne_lst[i]*2 + po_lst[(k-1)-(i+1)])
for i,j in enumerate(po_lst):
    if k-(i+1)>0 and len(ne_lst) > (k-1)-(i+1):
        res = min(res, po_lst[i]*2 + ne_lst[(k-1)-(i+1)])
print(res)
