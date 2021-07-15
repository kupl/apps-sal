# +1/-1の折れ線で表したとき
# 「0で終わる」かつ「途中で0未満にならない」を満たせば良い

# あとは貪欲を上手い事使う


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    a = []
    b = []
    for _ in range(n):
        s = input().rstrip()
        # 最終的に上がる量/最下点
        up, down = 0, 0
        for i in s:
            if i == ')':
                up -= 1
                if down > up:
                    down = up
            else:
                up += 1
        if up >= 0:
            a.append((down, up))
        else:
            b.append((down-up, -up))

    a.sort(key=lambda a: a[0],reverse=True)
    b.sort(key=lambda a: a[0],reverse=True)

    left, right = 0, 0

    for d, u in a:
        if left+d < 0:
            print('No')
            break
        else:
            left += u
    else:
        for d, u in b:
            if right+d < 0:
                print('No')
                break
            else:
                right += u
        else:
            if left == right:
                print('Yes')
            else:
                print('No')
    
def __starting_point():
    main()
__starting_point()
