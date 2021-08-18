b = input()
f = int(b)
c = []
N = 0
for i in range(len(b)):
    c.append(int(b[i]))
d = f // int(sum(c))
e = f / int(sum(c))

if d == e:
    print("Yes")
else:
    print("No")
