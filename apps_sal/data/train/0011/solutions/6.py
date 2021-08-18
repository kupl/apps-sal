import math
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        s = input().rstrip()
        a1 = []
        a2 = []
        ws = {'W': 1, 'S': -1}
        ad = {'A': 1, 'D': -1}
        for c in s:
            if c in ('W', 'S'):
                a1.append(ws[c])
            else:
                a2.append(ad[c])
        pref_a1 = [0] + a1.copy()
        pref_a2 = [0] + a2.copy()
        for i in range(1, len(pref_a1)):
            pref_a1[i] += pref_a1[i - 1]
        for i in range(1, len(pref_a2)):
            pref_a2[i] += pref_a2[i - 1]

        def canDecrease(a):
            _min = min(a)
            _max = max(a)

            _min_rindex = a.index(_min)
            for i in range(_min_rindex, len(a)):
                if a[i] == _min:
                    _min_rindex = i
            _max_index = a.index(_max)
            if _max_index > _min_rindex:
                return True

            _max_rindex = a.index(_max)
            for i in range(_max_rindex, len(a)):
                if a[i] == _max:
                    _max_rindex = i
            _min_index = a.index(_min)
            if _max_rindex < _min_index:
                return True

            return False

        x = max(pref_a1) - min(pref_a1)
        y = max(pref_a2) - min(pref_a2)
        res = (x + 1) * (y + 1)
        if x > 1 and canDecrease(pref_a1):
            res = min(res, x * (y + 1))
        if y > 1 and canDecrease(pref_a2):
            res = min(res, (x + 1) * y)

        print(res)


def __starting_point():
    main()


__starting_point()
