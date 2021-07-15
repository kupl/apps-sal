n, c = list(map(int, input().split()))

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

r = [0]
p = [0]
for i in range(n-1):
    x1 = r[-1] + a[i]

    y1 = p[-1] + b[i]
    if i == 0:
        y1 += c
    p.append(y1)

    #print("x1:", x1)
    #print("y1:", y1)

    if r[-1] < p[-1]:
        z1 = r[-1] + b[i] + c
        #print("z1", z1)
        if z1 < y1:
            y1 = z1
            p[-1] = z1
    #print("----")
    if x1 < y1:
        r.append(x1)
    else:
        r.append(y1)

print(*r)
# print(p)


