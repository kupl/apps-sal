a = input()
c = []
for i in a:
    c.append(i)

d = set(c)

if len(d) < len(c):
    print("no")
else:
    print("yes")
