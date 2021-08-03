l = [int(x) for x in input().split('+')]
l.sort()
for x in l[:-1]:
    print(x, end='+')
print(l[len(l) - 1])
