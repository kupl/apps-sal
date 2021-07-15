n, x = map(int, input().split())
llist = list(map(int, input().split()))
dlist = [0]
d = 0
for i in llist:
    d += i
    dlist.append(d)
print(sum([i<=x for i in dlist]))
