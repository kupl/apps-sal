n = int(input())
d = []
for i in range(n):
    a, b = input().split()
    f = False
    for x in d:
        if a == x[1]:
            x[1] = b
            f = True
            break
    if not f:
        d.append([a, b])

print(len(d))
for x in d:
    print(x[0], x[1])
