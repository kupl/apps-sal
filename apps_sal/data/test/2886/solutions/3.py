
# -*- coding: UTF-8 -*-

import sys
import re


def std_in():
    return sys.stdin.readline().strip()


def first_match_of_pattern(text, pattern):
    if type(text) != str:
        text = str(text)

    re_patter = re.compile(pattern)
    ans = re_patter.findall(text)
    if ans:
        return ans[0]
    return ""


def _main():
    s = std_in()
    az = [chr(i) for i in range(97, 97+26)]
    for c in az:
        p = r"[" + c + r"][a-z][" + c + "]"
        mt = first_match_of_pattern(s, p)
        if mt != "":
            first = s.find(mt) + 1
            end = first + len(mt) - 1
            print((first, end))
            break

        p = r"[" + c + r"][" + c + "]"
        mt = first_match_of_pattern(s, p)
        if mt != "":
            first = s.find(mt) + 1
            end = first + len(mt) - 1
            print((first, end))
            break
    else:
        print((-1, -1))


def __starting_point():
    _main()

__starting_point()
