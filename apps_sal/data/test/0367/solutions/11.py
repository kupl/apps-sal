"""
Codeforces Educational Round 2

Problem 600 C. Make Palindrome

@author yamaton
@date 2015-11-30
"""

import collections


def solve(s):
    n = len(s)
    chars = collections.Counter(s)
    base = sorted(c for c in chars if chars[c] >= 2 for _ in range(chars[c] // 2))
    chars_odd = sorted(c for c in chars if chars[c] % 2 == 1)

    if n % 2 == 0:
        keep = len(chars_odd) // 2
        chars_selected = sorted(base + chars_odd[:keep])
        return chars_selected + chars_selected[::-1]
    else:
        keep = len(chars_odd) // 2
        chars_selected = sorted(base + chars_odd[:keep])
        middle = chars_odd[keep]
        return chars_selected + [middle] + chars_selected[::-1]


def main():
    s = input().strip()
    result = solve(s)
    print(''.join(result))


def __starting_point():
    main()

__starting_point()
