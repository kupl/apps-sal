# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 22:47
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : B. Game with string.py


def main():
    s = input()
    times, stack = 0, []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()
            times += 1
    print('Yes' if times % 2 else 'No')


def __starting_point():
    main()


__starting_point()
