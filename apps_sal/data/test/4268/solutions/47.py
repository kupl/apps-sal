import itertools 
N, D = map(int, input().split())
count = 0
lst = []
for n in range(N):
    X = list(map(int, input().split()))
    lst.append(X)
c = list(itertools.combinations(lst, 2))

lst2 = []
for a in c:
    d2 = 0
    for x, y in zip(a[0], a[1]):
        s = (x - y) ** 2
        d2 += s
    d = d2 ** 0.5
    if d.is_integer():
        lst2.append(d)
print(len(lst2))
