import io
import sys
import math
CASES = 'abcdefghijklmnopqrstuvwxyz'


def format_multi_line_answer(lst):
    ans = ''
    ans += f'{len(lst)}\n'
    for y in lst:
        ans += f'{y}\n'
    return ans


def is_unballance(s):
    if len(s) == 2 and s[0] == s[1]:
        return True
    if len(s) == 3 and s[0] == s[2]:
        return True
    return False


def solve(s):
    ans_l = []
    has_unbalance = False
    (a, b) = (-1, -1)
    for c in CASES:
        i = s.find(c)
        ii = s.find(c, i + 1)
        while ii != -1:
            if ii - i < 3 and is_unballance(s[i:ii + 1]):
                (a, b) = (i + 1, ii + 1)
                has_unbalance = True
                break
            i = ii
            ii = s.find(c, i + 1)
        if has_unbalance:
            break
    return f'{a} {b}'


def main():
    s = input()
    ans = str(solve(s))
    print(ans)
    return ans


_DEB = 0
_INPUT = 'abcaxa\n'
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
