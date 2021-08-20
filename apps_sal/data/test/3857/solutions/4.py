n = int(input())
val = [[]]
for x in sorted((int(x) for x in input().split())):
    for l in val:
        if x >= len(l):
            l.append(x)
            break
    if len(val[-1]) > 0:
        val.append([])
print(len(val) - 1)
