o = list(input())
e = list(input())
s = []
t = ""
if len(o+e) % 2 == 0:
    for i in range(int(len(o+e)/2)):
        s.append(o[i]+e[i])
    t = t.join(s)
else:
    for i in range(int(len(o+e)/2)):
        s.append(o[i]+e[i])
    t = t.join(s)
    t = t + o[int(len(o+e)/2)]

print(t)

