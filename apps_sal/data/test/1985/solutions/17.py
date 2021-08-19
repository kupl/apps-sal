def R():
    return map(int, input().split())


(k, n) = R()
(a, b) = (list(R()), list(R()))
c = [a[0]]
for i in range(1, k):
    c.append(c[-1] + a[i])
c = set(c)
(s, cur) = (set(), 0)
for x in a:
    cur += x
    new = b[0] - cur
    for y in b[1:]:
        if y - new not in c:
            break
    else:
        s.add(new)
print(len(s))
