n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos_and = [
    {(0, 1), (0, 2), (0, 3), (0, 0), (1, 2)},
    {(1, 3), (1, 1)},
    {(2, 3), (2, 2)},
    {(3, 3)}
]
pos_or = [
    {(0, 0)},
    {(0, 1), (1, 1)},
    {(0, 2), (2, 2)},
    {(0, 3), (1, 3), (2, 3), (3, 3), (1, 2)}
]


res1 = []
flag1 = False
for i in range(n - 1):
    pairs = [x for x in pos_and[b[i]].intersection(pos_or[a[i]])]
    pairs.sort()
    if len(pairs) == 0:
        flag1 = True
        break
    for pair in pairs:
        rev_pair = (pair[1], pair[0])
        if len(res1) == 0:
            res1.append(pair[0])
            res1.append(pair[1])
            break
        if res1[-1] == pair[0]:
            res1.append(pair[1])
            break
        elif res1[-1] == rev_pair[0]:
            res1.append(rev_pair[1])
            break
    if len(res1) != i + 2:
        flag1 = True
        break
res2 = []
flag2 = False
for i in range(n - 1):
    pairs = [x for x in pos_and[b[i]].intersection(pos_or[a[i]])]
    pairs.sort()
    if len(pairs) == 0:
        flag2 = True
        break
    for pair in pairs:
        rev_pair = (pair[1], pair[0])
        if len(res2) == 0:
            res2.append(rev_pair[0])
            res2.append(rev_pair[1])
            break
        if res2[-1] == pair[0]:
            res2.append(pair[1])
            break
        elif res2[-1] == rev_pair[0]:
            res2.append(rev_pair[1])
            break
    if len(res2) != i + 2:
        flag2 = True
        break
if flag1 and flag2 and a[0] == 3 and b[0] == 0:
    res1 = []
    flag1 = False
    for i in range(n - 1):
        pairs = [x for x in pos_and[b[i]].intersection(pos_or[a[i]])]
        pairs.sort()
        if len(pairs) == 0:
            flag1 = True
            break
        for pair in pairs:
            rev_pair = (pair[1], pair[0])
            if len(res1) == 0:
                res1.append(pairs[1][0])
                res1.append(pairs[1][1])
                break
            if res1[-1] == pair[0]:
                res1.append(pair[1])
                break
            elif res1[-1] == rev_pair[0]:
                res1.append(rev_pair[1])
                break
        if len(res1) != i + 2:
            flag1 = True
            break
    res2 = []
    flag2 = False
    for i in range(n - 1):
        pairs = [x for x in pos_and[b[i]].intersection(pos_or[a[i]])]
        pairs.sort()
        if len(pairs) == 0:
            flag2 = True
            break
        for pair in pairs:
            rev_pair = (pair[1], pair[0])
            if len(res2) == 0:
                res2.append(pairs[1][1])
                res2.append(pairs[1][0])
                break
            if res2[-1] == pair[0]:
                res2.append(pair[1])
                break
            elif res2[-1] == rev_pair[0]:
                res2.append(rev_pair[1])
                break
        if len(res2) != i + 2:
            flag2 = True
            break
if not flag2:
    print("YES")
    print(*res2)
elif not flag1:
    print("YES")
    print(*res1)
else:
    print("NO")
