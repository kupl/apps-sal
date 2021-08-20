(_, s) = (input(), input())
MAX_H = 1 + 2 * max((s.count('[', 0, i) - s.count(']', 0, i) for i in range(len(s) + 1)))


def line(d):
    return '+'.join((' ' * d, '|' * (MAX_H - 2 * d - 2), ' ' * d))


def draw(s, i, d):
    return [line(d)] if s[i] == '[' else ([' ' * MAX_H] * 3 if s[i - 1] == '[' else []) + [line(d - 1)]


[print(''.join(x).replace('+ ', '+-').replace(' +', '-+')) for x in zip(*sum((draw(s, i, s.count('[', 0, i) - s.count(']', 0, i)) for i in range(len(s))), []))]
