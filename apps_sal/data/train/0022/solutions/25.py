cases = int(input())
for _ in range(cases):
    (n, k) = [int(s) for s in input().split()]
    mind = -1
    for _ in range(k - 1):
        if mind == 0:
            break
        s = str(n)
        (mind, maxd) = (int(s[0]), int(s[0]))
        for l in s:
            value = int(l)
            if value > maxd:
                maxd = value
            elif value < mind:
                mind = value
            if mind == 0:
                break
        n += maxd * mind
    print(n)
