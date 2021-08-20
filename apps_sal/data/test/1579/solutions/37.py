def main():
    from collections import defaultdict
    import sys

    def r():
        return sys.stdin.readline().strip()

    def R():
        return list(map(int, r().split()))
    N = int(r())
    Dic = defaultdict(list)
    V = 10 ** 5 + 5
    Arrived = [False] * (2 * V)
    for _ in range(N):
        (x, y) = R()
        y += V
        Dic[x].append(y)
        Dic[y].append(x)
    ans = 0
    task = []
    for (k, v) in Dic.items():
        if Arrived[k]:
            continue
        Arrived[k] = True
        if k < V:
            cntx = 1
            cnty = 0
        else:
            cntx = 0
            cnty = 1
        cntdot = 0
        task.extend(v)
        cntdot += len(v)
        while task:
            s = task.pop()
            if Arrived[s]:
                continue
            if s < V:
                cntx += 1
            else:
                cnty += 1
            Arrived[s] = True
            task.extend(Dic[s])
            cntdot += len(Dic[s])
        ans += cntx * cnty - cntdot // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
