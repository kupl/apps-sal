n = int(input())
d = {}
for i in range(n):
    s = input()
    for w in d:
        if s.count(w) == 0:
            d[w] = 0
    for c in s:
        if i == 0:
            d[c] = d.get(c, 0) + 1
        else:
            d[c] = min(d.get(c, 0), s.count(c))

li = []
for w in d:
    for i in range(d[w]):
        li.append(w)
li.sort()
print("".join(li))
