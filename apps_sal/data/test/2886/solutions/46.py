import io
import sys
import math


def solve(s):
    len_s = len(s)
    (a, b) = (-1, -1)
    for i in range(len_s):
        if len_s - i > 1 and s[i] == s[i + 1]:
            (a, b) = (i + 1, i + 2)
            break
        if len_s - i > 2 and s[i] == s[i + 2]:
            (a, b) = (i + 1, i + 3)
            break
    return f'{a} {b}'


def main():
    s = input()
    ans = str(solve(s))
    print(ans)
    return ans


_DEB = 0
_INPUT = 'aba\n'
_EXPECTED = '2 5\n'


def logd(str):
    """usage:
    if _DEB: logd(f"{str}")
    """
    if _DEB:
        print(f'[deb] {str}')


def __starting_point():
    if _DEB:
        sys.stdin = io.StringIO(_INPUT)
        print('!! Debug Mode !!')
    ans = main()
    if _DEB:
        print()
        if _EXPECTED.strip() == ans.strip():
            print('!! Success !!')
        else:
            print(f'!! Failed... !!\nANSWER:   {ans}\nExpected: {_EXPECTED}')


__starting_point()
