import io
import os
from collections import defaultdict
from sys import stdin, stdout


def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sorted(set(a))
    d = {}
    for val in s:
        d[val] = 0
    for val in a:
        d[val] += 1
    max_len = 1
    res = [a[0]]
    for j in range(len(s) - 1):
        if d[s[j]] == 1 and d[s[j + 1]] == 1 and (s[j + 1] - s[j] == 1):
            max_len = 2
            res = [s[j], s[j + 1]]
            break
    start = 0
    while start < len(s) and d[s[start]] == 1:
        start += 1
    while start < len(s):
        if start < len(s):
            l = start
            r = start
            while l > 0 and d[s[l - 1]] > 1 and (s[l] - s[l - 1] == 1):
                l -= 1
            while r < len(s) - 1 and d[s[r + 1]] > 1 and (s[r + 1] - s[r] == 1):
                r += 1
            if l > 0 and s[l] - s[l - 1] == 1:
                l -= 1
            if r < len(s) - 1 and s[r + 1] - s[r] == 1:
                r += 1
            total = 0
            for j in range(l, r + 1):
                total += d[s[j]]
            if total > max_len:
                max_len = total
                res = []
                for j in range(l, r + 1):
                    res.append(s[j])
                    d[s[j]] -= 1
                for j in range(r, l - 1, -1):
                    while d[s[j]] > 0:
                        res.append(s[j])
                        d[s[j]] -= 1
            start = r + 1
            while start < len(s) and d[s[start]] == 1:
                start += 1
    print(len(res))
    print(*res)


def __starting_point():
    main()


__starting_point()
