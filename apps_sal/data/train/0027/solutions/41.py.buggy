def ans():
    nonlocal lst
    d = dict()
    for i in lst:
        s2, delit = st2(i)
        if delit not in d:
            d[delit] = s2
            continue
        if d[delit] < s2:
            d[delit] = s2
    return sum(d.values())


def st2(num):
    c = 0
    while (num % 2 == 0) and num != 0:
        num = num >> 1
        c += 1
    return [c, num]


lst = []
for i in range(int(input())):
    t = int(input())
    lst = list(map(int, input().split()))
    print(ans())
