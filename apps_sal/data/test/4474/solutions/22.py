q = int(input())
out = []
for i in range(q):
    n = int(input())
    mm = 1
    sts = []
    while mm < n:
        sts.append(mm)
        mm *= 3
    sts.append(mm)
    m = sum(sts)
    for i in range(len(sts) - 1, -1, -1):
        if m - sts[i] < n:
            continue
        else:
            m -= sts[i]
    out.append(str(m))
print('\n'.join(out))
