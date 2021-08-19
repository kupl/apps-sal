3


def readint():
    return int(input())


def readline():
    return [int(c) for c in input().split()]


def compute_time(a, l):
    cnt = 0
    prev = -1
    for e in a:
        if e > l and prev <= l:
            cnt += 1
        prev = e
    return cnt


def main():
    (n, m, l) = readline()
    a = readline()
    time = compute_time(a, l)
    for i in range(m):
        q = readline()
        if q[0] == 0:
            print(time)
        else:
            (p, d) = (q[1], q[2])
            is_left_short = True if p == 1 or a[p - 2] <= l else False
            is_right_short = True if p == n or a[p] <= l else False
            if is_left_short and is_right_short and (a[p - 1] <= l) and (a[p - 1] + d > l):
                time += 1
            elif not is_left_short and (not is_right_short) and (a[p - 1] <= l) and (a[p - 1] + d > l):
                time -= 1
            a[p - 1] += d


def __starting_point():
    main()


__starting_point()
