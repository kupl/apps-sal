def main():
    import sys
    import copy
    from bisect import bisect_right
    from collections import defaultdict
    input = sys.stdin.readline
    (s, t) = (input().strip(), input().strip())
    lens = len(s)
    index_list = defaultdict(list)
    leng = defaultdict(int)
    for (i, ss) in enumerate(s):
        index_list[ss].append(i)
    for (s, i) in index_list.items():
        if i:
            leng[s] = len(index_list[s])
    prev = -1
    ans = 0
    for tt in t:
        if tt not in leng:
            print(-1)
            return False
        p = bisect_right(index_list[tt], prev)
        if p < leng[tt]:
            prev = index_list[tt][p]
        else:
            prev = index_list[tt][0]
            ans += lens
    print(ans + prev + 1)


def __starting_point():
    main()


__starting_point()
