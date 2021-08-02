word = input()

BRACKETS = [
    ('<', '>'),
    ('{', '}'),
    ('[', ']'),
    ('(', ')'),
]

OPENING = [b[0] for b in BRACKETS]

MATCH = dict(BRACKETS)

IMPOSSIBLE = 'Impossible'


def is_opening(w):
    return w in OPENING


def same_kind(wo, wc):
    return MATCH[wo] == wc


def solve(word):
    temp = []
    result = 0
    for w in word:
        if is_opening(w):
            temp.append(w)
        else:
            if len(temp) == 0:
                return IMPOSSIBLE
            wo = temp.pop()
            if not is_opening(wo):
                return IMPOSSIBLE
            if not same_kind(wo, w):
                result += 1
    if len(temp) != 0:
        return IMPOSSIBLE
    return result


print(solve(word))
