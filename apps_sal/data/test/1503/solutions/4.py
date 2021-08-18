def intersection(a, b):
    ret = (max(a[0], b[0]), min(a[1], b[1]))
    if ret[0] >= ret[1]:
        return (-1, -1)
    return ret


def calc(n, m, interval):
    ret = 0
    it_list = [(0, n - 1)]
    for i in range(m):
        interval_now = interval[i]

        if len(interval_now) == 0:
            return 0
        next_list = []
        j = 0
        k = 0
        while j < len(it_list) and k < len(interval_now):
            n1 = it_list[j]
            n2 = interval_now[k]
            inter = intersection(n1, n2)
            if inter[0] == -1:
                if n1[0] < n2[0]:
                    j += 1
                else:
                    k += 1
                continue
            next_list.append(inter)
            if n1[1] < n2[1]:
                j += 1
            else:
                k += 1
        it_list = next_list
        if len(it_list) == 0:
            return 0
    for it in it_list:
        l = it[1] - it[0] + 1
        ret += l * (l + 1) // 2 - l
    return ret


def main():
    n, m = [int(x) for x in input().split(" ")]
    a = []
    for i in range(m):
        now = list([int(x) for x in input().split(" ")])
        a.append(now)
    ans = n
    if m == 1:
        print(n * (n + 1) // 2)
        return
    ch = [0 for i in range(n)]
    for i in range(n):
        ch[a[0][i] - 1] = i
    for i in range(m):
        for j in range(n):
            a[i][j] = ch[a[i][j] - 1]
    interval = []
    for i in range(m):
        a_now = a[i]
        l = 0
        r = 0
        now = []
        for j in range(1, n):
            if a_now[j] == a_now[j - 1] + 1:
                r += 1
            else:
                if r > l:
                    it = (a_now[l], a_now[r])
                    now.append(it)
                l = j
                r = j
        if r > l:
            it = (a_now[l], a_now[r])
            now.append(it)
        now = sorted(now, key=lambda x: x[0])
        interval.append(now)
    ans += calc(n, m, interval)
    print(ans)


def __starting_point():
    main()


__starting_point()
