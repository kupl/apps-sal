n = int(input())
l1 = 0
l2 = -1
r1 = 0
r2 = -1
ls = []
rs = []
for i in range(n):
    l, r = map(int, input().split())
    ls.append(l)
    rs.append(r)
    if i == 0:
        continue
    if l > ls[l1] or l == ls[l1] and r <= rs[l1]:
        l2 = l1
        l1 = i
    elif l2 == -1 or l > ls[l2] or l == ls[l2] and r <= ls[l2]:
        l2 = i
    if r < rs[r1] or r == rs[r1] and l > ls[r1]:
        r2 = r1
        r1 = i
    elif r2 == -1 or r < rs[r2] or r == rs[r2] and l > ls[r2]:
        r2 = i
if l1 == r1:
    ans = rs[r2] - ls[l2]
elif ls[l1] - ls[l2] > rs[r2] - rs[r1]:
    ans = rs[r1] - ls[l2]
else:
    ans = rs[r2] - ls[l1]
print(max(ans, 0))
