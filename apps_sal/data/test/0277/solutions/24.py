n, a, b = [int(x) for x in input().split()]

l1 = [x for x in range(1, n + 1)]
l2 = []
res = 0
found = False
while (not found):
    res += 1
    for i in range(0, len(l1), 2):
        if l1[i] in [a, b] and l1[i + 1] in [a, b]:
            found = True
            if len(l1) == 2:
                res = "Final!"
            break
        if l1[i] in [a, b]:
            l2.append(l1[i])
        else:
            l2.append(l1[i + 1])

    l1 = l2
    l2 = []

print(res)
