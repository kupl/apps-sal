def razl(a):
    if a % 2 == 0:
        r = [0, 0]
    else:
        r = [0, 0]
    while a % 2 == 0:
        a = a / 2
        r[0] += 1
    r[1] = a
    return r


ans = []
for i in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    c = []
    for j in range(a):
        c.append(razl(b[j]))
    c.sort()
    d = {}
    for j in range(len(c)):
        d[c[j][1]] = c[j][0]
    ans.append(sum(list(d.values())))
for i in ans:
    print(i)
