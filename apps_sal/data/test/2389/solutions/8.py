def update_vrs(vrs, idx, s):
    if idx == 0:
        vrs[s[0]] += 1
        vrs[s[1]] -= 1
    elif idx == 1:
        vrs[s[0]] -= 1
        vrs[s[1]] += 1
    else:
        raise ValueError()


def process1(vrs, lst_s):
    selects = []
    for s in lst_s:
        if vrs[s[0]] == 0 and vrs[s[1]] == 0:
            return (False, None)
        elif vrs[s[0]] == 0:
            selects.append(s[0])
            update_vrs(vrs, 0, s)
        else:
            selects.append(s[1])
            update_vrs(vrs, 1, s)
    return (True, selects)


def process2(vrs, lst_s):
    selects = []
    for (i, s) in enumerate(lst_s):
        if vrs[s[0]] == 0 and vrs[s[1]] == 0:
            return (False, None)
        elif vrs[s[0]] == 0:
            selects.append(s[0])
            update_vrs(vrs, 0, s)
        elif vrs[s[1]] == 0:
            selects.append(s[1])
            update_vrs(vrs, 1, s)
        elif i == len(lst_s) - 1:
            selects.append(s[0])
        else:
            next_s = lst_s[i + 1]
            if s[0] in next_s:
                selects.append(s[0])
                update_vrs(vrs, 0, s)
            else:
                selects.append(s[1])
                update_vrs(vrs, 1, s)
    return (True, selects)


def main():
    vrs = {}
    (n, vrs['A'], vrs['B'], vrs['C']) = [int(v) for v in input().split(' ')]
    lst_s = []
    for _ in range(n):
        lst_s.append(input().strip())
    sum_abc = vrs['A'] + vrs['B'] + vrs['C']
    if sum_abc == 0:
        ans = False
    elif sum_abc == 1:
        (ans, selects) = process1(vrs, lst_s)
    else:
        (ans, selects) = process2(vrs, lst_s)
    if ans is True:
        print('Yes')
        for s in selects:
            print(s)
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
