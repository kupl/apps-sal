l = input().split()
l = [int(x) for x in l]
x = l[0]
y = l[1]
a = l[2]
b = l[3]


r = []
for i in range(a, x+1):
    for j in range(b, y+1):
        if i>j:
            r.append((i, j))
        else:
            break

print(len(r))
for x in r:
    print(x[0], x[1])


