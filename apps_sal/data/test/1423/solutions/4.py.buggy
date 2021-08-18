n, l, r = list(map(int, input().split()))
a = list(map(int, input().split()))
p = list(map(int, input().split()))

order = dict()

for i in range(len(p)):
    order[p[i]] = i

curr = -100000000000
b = [-1] * n
for i in range(1, n + 1):
    if i == 1:
        b[order[i]] = l
        curr = b[order[i]] - a[order[i]]
        continue
    b[order[i]] = max(l, curr + 1 + a[order[i]])
    curr = b[order[i]] - a[order[i]]

for i in b:
    if i > r:
        print(-1)
        return
print(*b)
