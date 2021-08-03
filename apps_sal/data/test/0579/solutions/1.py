import numpy as np


def main():
    n, k = list(map(int, input().split()))
    p = [int(i) - 1 for i in input().split()]
    c = [int(i) for i in input().split()]

    seen = set()
    loop_list = []
    for start in range(n):
        v = start
        loop = []
        while v not in seen:
            seen.add(v)
            loop.append(c[v])
            v = p[v]
        seen.add(v)
        if loop:
            loop_list.append(np.array(loop))

    ans = min(c)
    for loop in loop_list:
        loop_len = len(loop)
        loop_num = k // loop_len
        loop_mod = k % loop_len
        loop_sum = sum(loop)
        table = np.zeros((loop_len, loop_len), dtype=int)
        table[0] = loop.cumsum()
        table[:, -1] = loop_sum
        for i in range(loop_len - 1):
            table[i + 1, :-1] = (table[i] - loop[i])[1:]
        ans = max(table[:, :min(loop_len, k)].max(), ans)
        if loop_num > 0:
            ans = max(loop_sum * (loop_num - 1) + table[:, :loop_len].max(), ans)
            if loop_mod > 0:
                ans = max(loop_sum * loop_num + table[:, :loop_mod].max(), ans)
    print(ans)


def __starting_point():
    main()


__starting_point()
