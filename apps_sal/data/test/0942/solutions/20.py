n = int(input())
a = [int(element) for element in input().split(' ')]
b = dict()
for i in range(n):
    try:
        b[a[i]] += 1
    except:
        b[a[i]] = 1
c = [(b[k] % (n-k)) == 0 for k in list(b.keys())]
d = [b[k] for k in a]

if all(c):
    print("Possible")
    types = dict()
    hat = 1
    for k in list(b.keys()):
        pergroup = n-k
        groups = b[k] // pergroup
        hatsgroup = list()
        for i in range(groups):
            for j in range(pergroup):
                hatsgroup.append(hat)
            hat += 1
        types[k] = hatsgroup
    hats = list()
    for i in range(n):
        hats.append(types[a[i]].pop())
    print(' '.join(str(e) for e in hats))

else:
    print("Impossible")

