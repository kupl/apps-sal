import string
import copy


def solution(s):
    if len(s) == 0:
        return ''
    if len(s) % 2 == 1:
        return ':('

    if s[0] not in '(?':
        return ':('
    if s[-1] not in ')?':
        return ':('

    s = s[1:-1]
    n = len(s)
    n1 = s.count('(')
    n2 = s.count(')')

    if n1 > n // 2 or n2 > n // 2:
        return ':('

    n1 = n // 2 - n1
    n2 = n // 2 - n2
    ans = []
    for i in range(len(s)):
        if s[i] != '?':
            ans.append(s[i])
        elif n1 > 0:
            ans.append('(')
            n1 -= 1
        else:
            ans.append(')')

    n = 0
    for c in ans:
        if c == '(':
            n += 1
        else:
            n -= 1
        if n < 0:
            return ':('

    if n != 0:
        return ':('

    return "(%s)" % ''.join(ans)


def parser():
    n = int(input())
    s = input()
    return s


def output(s):
    print(s)


def main():
    args = parser()
    result = solution(args)
    output(result)


def __starting_point():
    main()


__starting_point()
