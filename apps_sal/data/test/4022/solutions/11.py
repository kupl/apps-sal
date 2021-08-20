n = int(input())
max_l1 = 0
max_l2 = 0
min_r1 = 10000000000
min_r2 = 10000000000
ind1 = 0
ind2 = 0
for i in range(n):
    (l, r) = map(int, input().split())
    if l >= max_l1:
        max_l2 = max_l1
        max_l1 = l
        ind1 = i
    elif l >= max_l2:
        max_l2 = l
    if r <= min_r1:
        min_r2 = min_r1
        min_r1 = r
        ind2 = i
    elif r <= min_r2:
        min_r2 = r
if ind1 == ind2:
    print(min_r2 - max_l2)
else:
    print(max(min_r2 - max_l1, min_r1 - max_l2, 0))
