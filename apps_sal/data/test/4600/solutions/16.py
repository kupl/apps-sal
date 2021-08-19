import numpy as np
import sys
input = sys.stdin.readline


def main():
    (n, m) = map(int, input().split())
    wa_answers = np.zeros(n + 1, dtype=int)
    ac_flag = np.zeros(n + 1, dtype=int)
    for i in range(m):
        (no, result) = input().split()
        no = int(no)
        if result == 'AC' and ac_flag[no] == 0:
            ac_flag[no] = 1
        if result == 'WA' and ac_flag[no] == 0:
            wa_answers[no] += 1
    print(sum(ac_flag), sum(ac_flag * wa_answers))


def __starting_point():
    main()


__starting_point()
