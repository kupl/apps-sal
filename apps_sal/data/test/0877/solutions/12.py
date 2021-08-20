def compute():
    (n, m) = [int(s) for s in input().split()]
    p = {}
    for i in range(m):
        (u, v) = [int(s) for s in input().split()]
        if u > v:
            if p.get(u) == 2:
                return 0
            if p.get(v) == 1:
                return 0
            p[u] = 1
            p[v] = 2
        else:
            if p.get(v) == 2:
                return 0
            if p.get(u) == 1:
                return 0
            p[v] = 1
            p[u] = 2
    (div1, div2) = ([], [])
    for (k, v) in list(p.items()):
        if v == 1:
            div1.append(k)
        else:
            div2.append(k)
    p_left = [i for i in range(1, n + 1) if i not in p]
    if not div1:
        if p_left:
            div1.append(p_left[-1])
            p_left.remove(p_left[-1])
        else:
            return 0
    if not div2:
        if p_left:
            div2.append(p_left[0])
            p_left.remove(p_left[0])
        else:
            return 0
    div1_easiest = min(div1)
    div2_hardest = max(div2)
    if div2_hardest > div1_easiest:
        return 0
    res = 1
    for i in range(len(p_left)):
        if p_left[i] > div1_easiest:
            pass
        elif p_left[i] < div2_hardest:
            pass
        else:
            res += 1
    return res


res = compute()
print(res)
