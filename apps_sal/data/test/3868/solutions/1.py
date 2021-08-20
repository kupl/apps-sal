def main():
    (n, m, k) = list(map(int, input().split()))
    (ff, tt) = ([], [])
    for _ in range(m):
        (d, f, t, c) = list(map(int, input().split()))
        if f:
            ff.append((d, f, c))
        else:
            tt.append((-d, t, c))
    for ft in (ff, tt):
        (cnt, costs) = (n, [1000001] * (n + 1))
        ft.sort(reverse=True)
        while ft:
            (day, city, cost) = ft.pop()
            oldcost = costs[city]
            if oldcost > cost:
                costs[city] = cost
                if oldcost == 1000001:
                    cnt -= 1
                    if not cnt:
                        break
        else:
            print(-1)
            return
        total = sum(costs) - 1000001
        l = [(day, total)]
        while ft:
            (day, city, cost) = ft.pop()
            oldcost = costs[city]
            if oldcost > cost:
                total -= oldcost - cost
                costs[city] = cost
                if l[-1][0] == day:
                    l[-1] = (day, total)
                else:
                    l.append((day, total))
        if ft is ff:
            ff = l
        else:
            tt = l
    (l, k) = ([], -k)
    (d, c) = tt.pop()
    try:
        for (day, cost) in ff:
            while d + day >= k:
                (d, c) = tt.pop()
            if d + day < k:
                l.append(c + cost)
    except IndexError:
        pass
    print(min(l, default=-1))


def __starting_point():
    main()


__starting_point()
