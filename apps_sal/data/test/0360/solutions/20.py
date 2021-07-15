n = int(input())
l = []
r = []
for i in range(n):
    l1, r1 = map(int, input().split())
    l.append(l1)
    r.append(r1)
k = int(input())
res = 1
for el in l:
    if k < el:
        res += 1
print(res)
