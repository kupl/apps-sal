a, b, c ,d = map(int, input().split())
l = []
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l = sorted(l)
if l[0]+l[3] == l[1]+l[2]:
    print("Yes")
else:
    if l[0]+l[1]+l[2] == l[3]:
        print("Yes")
    else:
        print("No")
