#! usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    n, k = list(map(int, input().split()))
    s = input()

    cnt = [0] * 26
    idx = 0
    while idx < n:
        cur = idx
        while cur < n - 1 and s[cur + 1] == s[idx] and cur - idx + 1 < k:
            cur += 1

        if cur - idx + 1 == k:
            cnt[ord(s[idx]) - ord('a')] += 1
        idx = cur + 1

    print(max(cnt))


def __starting_point():
    main()


__starting_point()
