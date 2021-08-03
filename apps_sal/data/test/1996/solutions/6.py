n = int(input())
y = set()
opr = False
count = 0
for i in range(97, 123):
    y.add(chr(i))
for i in range(n):
    s = input()
    s = s.split(" ")
    a = s[1]
    if not opr:
        z = set()
        for j in a:
            z.add(j)
        if s[0] == "!":
            y = y.intersection(z)
        elif s[0] == ".":
            y = y.difference(z)
        elif s[0] == "?" and i != n - 1:
            q = set()
            q.add(s[1])
            y = y.difference(q)
        if len(y) == 1:
            opr = True
    else:
        if (s[0] == "?" and i != n - 1) or s[0] == "!":
            count += 1
print(count)
