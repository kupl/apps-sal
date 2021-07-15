import string, copy


def _value(c):
    return ord(c) - 97

def _char(i):
    return chr(i + 97)


def solution(s1, s2):
    s1 = [_value(c) for c in s1]
    s2 = [_value(c) for c in s2]

    # Sum
    sum_s = []
    tmp = 0
    for i in range(len(s1)-1, -1, -1):
        s = s1[i] + s2[i] + tmp
        tmp = s // 26
        sum_s.append(s % 26)
    if tmp:
        sum_s.append(tmp)

    sum_s = sum_s[::-1]

    # Div by 2
    tmp = 0
    result = []
    for i in range(len(sum_s)):
        s = sum_s[i]
        result.append((s + 26 * tmp) // 2)
        tmp = s % 2

    result = result[-len(s1):]
    result = [_char(i) for i in result]
    return ''.join(result)



#     tmp = 0
#     s = []
#     for c1, c2 in zip(s1, s2):
#         cur = _value(c1) + _value(c2) - tmp * 26
#         tmp = cur % 2
#         s.append(_char((cur + 1) // 2))
#     return ''.join(s)


def parser():
    n = int(input())
    s1 = input()
    s2 = input()
    return s1, s2


def output(s):
    print(s)


def main():
   args = parser()
   result = solution(*args)
   output(result)


def __starting_point():
    main()
__starting_point()
