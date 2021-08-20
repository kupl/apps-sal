(c1, c2, c3, c4) = list(map(int, input().split()))
(n, m) = list(map(int, input().split()))
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
buss = 0
for i in lst1:
    buss += min(c1 * i, c2)
buss = min(buss, c3)
tr = 0
for i in lst2:
    tr += min(c1 * i, c2)
tr = min(tr, c3)
print(min(c4, buss + tr))
