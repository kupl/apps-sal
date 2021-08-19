def main():

    def Technique_often_used():
        pass

    def naming_conventions():
        pass

    def visual_studio_code_shortcut():
        pass
    import sys
    from itertools import combinations, permutations
    from collections import deque, Counter
    from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest
    from copy import deepcopy, copy
    from functools import reduce
    from fractions import gcd

    def gcds(numbers):
        return reduce(gcd, numbers)

    def lcm(x, y):
        return x * y // gcd(x, y)

    def lcms(numbers):
        return reduce(lcm, numbers, 1)

    def R():
        return map(int, input().split())
    q = int(input())
    queries = [list(R()) for i in range(q)]
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
