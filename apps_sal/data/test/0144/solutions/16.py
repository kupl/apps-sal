def sum_o(s):
    if s == '':
        return 0
    res = 0
    for el in s:
        res += int(el)
    return res


def can(s, summ):
    if sum_o(s) == summ:
        return True
    res = ''
    for i in range(len(s)):
        wl = s[i]
        res += wl
        if sum_o(res) == summ:
            if can(s[i + 1:], summ):
                return True
            else:
                return False
        if sum_o(res) > summ:
            return False


def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        if can(s[i:], sum_o(s[:i])):
            return 'YES'
    return 'NO'


print(main())
