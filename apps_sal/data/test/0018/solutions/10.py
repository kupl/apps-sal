from itertools import takewhile

def f(s):
    t = []
    u = []
    chars = 'abcdefghijklmnopqrstuvwxyz'

    for c in chars:
        stack = list(takewhile(lambda x: x <= c, reversed(t)))
        count = len(stack)
        if count > 0:
            u += stack
            t = t[:-count]

        count = s.count(c)
        if count > 0:
            rindex = s.rindex(c)
            u += c * count
            t += [x for x in s[:rindex] if x != c]
            s = s[rindex + 1:]

    u += reversed(t)
    return ''.join(u)

print(f(input()))

