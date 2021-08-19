from bisect import bisect_left
from collections import defaultdict as dd


def main():
    s = input()
    t = input()
    n = len(s)
    dic = dd(list)
    for (idx, i) in enumerate(s * 2):
        dic[i].append(idx)
    (ans, p) = (0, -1)
    for i in t:
        if i not in dic.keys():
            print(-1)
            return
        p = dic[i][bisect_left(dic[i], p + 1)]
        if p >= n:
            p -= n
            ans += n
    print(ans + p + 1)


def __starting_point():
    main()


__starting_point()
