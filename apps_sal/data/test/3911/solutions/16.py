n = int(input())

v = []
for i in range(n):
    v.append(1)

    while len(v) >= 2 and v[-2] == v[-1]:
        x = v.pop()
        v.pop()
        v.append(x+1)

print(' '.join([str(x) for x in v]))


