(n, x) = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
m = min(l)
x -= 1
p = -1
for i in range(n):
    if l[i] == m:
        p = i
    if i == x and p != -1:
        break
for i in range(n):
    l[i] -= m
    l[p] += m
if x != p:
    i = (p + 1) % n
    while i != x:
        l[i] -= 1
        l[p] += 1
        i = (i + 1) % n
    l[p] += 1
    l[i] -= 1
for i in l:
    print(i, end=' ')
