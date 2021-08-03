def main():
    def Technique_often_used():
        # enumerate: for i, a in enumerate(a_list):
        # q, mod = divmod(a, b)
        # Functional Programming: filter, map, reduce
        pass

    def naming_conventions():
        # [s_1, s_2, s_3, ..., s_k] is named s_k
        # [[s_11, s_12, ..., s_1k], ..,[s_j1, s_j2, ..., s_jk] is named s_jk
        # [[b1,c1],[b2,c2],..,[bm,cm]] is named bc
        # if there is something strange in a list then I add _ to the list's name (ex:s_jk_)
        pass

    def visual_studio_code_shortcut():
        # visual studio code shortcut https://qiita.com/TakahiRoyte/items/cdab6fca64da386a690b
        # delete line: Ctrl+Shift+k
        # choose same words: Ctrl+Shift+l
        pass
    import sys
    from itertools import combinations, permutations  # https://docs.python.org/ja/3/library/itertools.html
    from collections import deque, Counter  # https://docs.python.org/ja/3/library/collections.html#collections.deque
    from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest  # https://docs.python.org/ja/3/library/heapq.html
    from copy import deepcopy, copy  # https://docs.python.org/ja/3/library/copy.html
    from functools import reduce
    from fractions import gcd  # Deprecated since version 3.5: Use math.gcd() instead.

    def gcds(numbers):
        return reduce(gcd, numbers)

    def lcm(x, y):
        return (x * y) // gcd(x, y)

    def lcms(numbers):
        return reduce(lcm, numbers, 1)

    # set the inputs
        # open(0).read() is a convenient method:
        # ex) n, m, *x = map(int, open(0).read().split())
        #     min(x[::2]) - max(x[1::2])
        # ex2) *x, = map(int, open(0).read().split())
        #     don't forget to add comma after *x if only one variable is used
        # ex1) n, k = R()
        # ex2) v = list(R())
        # ex3) bc = [list(R()) for i in range(m)]

    def R(): return map(int, input().split())
    q = int(input())
    queries = [list(R()) for i in range(q)]

    # q = 4
    # queries=[[1,4,2],[1,5,3],[1,-9,5],[1,1,-8],[2]]

    l = []
    r = []
    ans = 0
    for query in queries:
        if query[0] == 1:
            a = heappushpop(l, -query[1])
            b = heappushpop(r, query[1])
            heappush(l, -b)
            heappush(r, -a)
            ans += abs(b + a) + query[2]
        else:
            print(-l[0], ans)


def __starting_point():
    main()


__starting_point()
