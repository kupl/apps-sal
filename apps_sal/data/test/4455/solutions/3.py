from itertools import accumulate


def main():
    n, k = [int(_) for _ in input().split()]
    skills = [int(_) for _ in input().split()]

    b = [(r, i) for i, r in enumerate(skills)]
    b.sort()

    x = 0
    c = [0] * n
    cnt = 0
    for r, i in b:
        if r > x:
            cnt_less = cnt
        c[i] = cnt_less
        cnt += 1
        x = r

    for _ in range(k):
        u, v = [int(_) for _ in input().split()]
        u -= 1
        v -= 1
        if skills[u] > skills[v]:
            c[u] -= 1
        elif skills[v] > skills[u]:
            c[v] -= 1

    print(' '.join(map(str, c)))


def __starting_point():
    main()


__starting_point()
