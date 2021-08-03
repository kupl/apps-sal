n = int(input())
c = list(input())
for i in range(n - 1):
    t = []
    s = list(input())
    for j in c:
        if j in s:
            t.append(j)
            s.remove(j)
    c = t
c.sort()
print("".join(c))
