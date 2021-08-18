
from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int, input().split()))

    sum_dict = defaultdict(list)
    for r in range(n):
        tmp = 0
        for l in range(r, -1, -1):
            tmp += a[l]
            sum_dict[tmp].append((l + 1, r + 1))

    ret, blocks = 0, []
    for k, v in list(sum_dict.items()):
        right, tmp = -1, 0
        curr_list = []
        for s in v:
            if s[0] > right:
                tmp += 1
                curr_list.append(s)
                right = s[1]
        if tmp > ret:
            ret = tmp
            blocks = curr_list

    print(ret)
    for s in blocks:
        print(*s)


def __starting_point():
    main()


__starting_point()
