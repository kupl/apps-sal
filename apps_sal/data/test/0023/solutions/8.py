from collections import Counter
a = input()
b = input()


def is_subcounter(cnt1, cnt2):
    for key in cnt1:
        if key not in cnt2 or cnt1[key] > cnt2[key]:
            return False
    return True


def subtract_counters(cnt1, cnt2):
    result = Counter(cnt1)
    for (key, val) in list(cnt2.items()):
        assert val <= result[key]
        result[key] -= val
    return result


def go():
    ca = Counter(a)
    best = None
    for pos in range(len(a) - 1, -1, -1):
        cb_before = Counter(b[:pos])
        if not is_subcounter(cb_before, ca):
            continue
        cnt_left = subtract_counters(ca, cb_before)
        for (key, val) in list(cnt_left.items()):
            if val == 0:
                continue
            if key >= b[pos]:
                continue
            tail = sorted(''.join((key1 * (val1 if key1 != key else val1 - 1) for (key1, val1) in list(cnt_left.items()))), reverse=True)
            curr = b[:pos] + key + ''.join(tail)
            assert curr < b
            if best is None or curr > best:
                best = curr
    assert best is not None
    return best


def solve(a, b):
    assert len(a) <= len(b)
    if len(a) < len(b):
        return ''.join(sorted(a, reverse=True))
    elif Counter(a) == Counter(b):
        return b
    else:
        return go()


print(solve(a, b))
