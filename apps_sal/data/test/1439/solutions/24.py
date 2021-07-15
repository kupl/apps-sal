n, m = list(map(int, input().split()))
a = list([x%m for x in list(map(int, input().split()))])
h = {}

for el in a:
    h[el] = h.get(el, 0) + 1

for v in list(h.values()):
    if v % m == 0:
        print("YES")
        return

possible = set([])
for el in a:
    new = set([el])
    for candidate in possible:
       new.add((candidate + el)%m)

    possible |= new
    if 0 in possible:
        print("YES")
        return
print("NO")

