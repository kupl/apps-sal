def MultiJudge(l, p):
    count = 0
    before = True
    l.sort()
    h = [x for x in l if x <= 2 * p]
    if len(h) > 0 and max(h) > p:
        p = max(h)
    b = [x for x in l if x > 2 * p]
    while len(b) > 0:
        h = [x for x in l if x <= 2 * p]
        b = [x for x in l if x > 2 * p]
        if len(h) > 0 and max(h) > p:
            p = max(h)
            before = False
        if len(b) > 0 and before:
            p = p * 2
            count += 1
        before = True
    print(count)


p = int(input().split()[1])
l = [int(x) for x in input().split()]
MultiJudge(l, p)
