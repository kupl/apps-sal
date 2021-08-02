#
# from __future__ import division

# input = raw_input
import math


# Make simpler structure:
class Same:
    def __init__(self, col, size, fro, to):
        self.size = size
        self.col = col
        self.fro = fro
        self.to = to

    def __repr__(self):
        return "Same({},{}, [{},{}))".format(self.col, self.size, self.fro, self.to)


class Alter:
    def __init__(self, size, fro, to):
        self.size = size
        self.fro = fro
        self.to = to

    def __repr__(self):
        return "Alter({}, [{},{}))".format(self.size, self.fro, self.to)


def simpl(lst):
    lst = lst[0] + lst + lst[-1]
    res = []
    prv = None
    streak_same = 0
    same_starts = 0
    for pos, curr in enumerate(lst):
        #print(pos, curr, prv, streak_same, same_starts)
        if curr == prv:
            if streak_same == 0:
                same_starts = pos - 1
                streak_same = 2
            else: streak_same += 1
        else:
            if streak_same > 0:
                res.append(Same(prv, streak_same, same_starts, pos))
                assert streak_same == pos - same_starts
                same_starts = None
                streak_same = 0
        prv = curr
    if streak_same > 0:
        res.append(Same(prv, streak_same, same_starts, len(lst)))
        assert streak_same == len(lst) - same_starts

    # Insert alternating and strip the ends. First strip the ends (and change the indices):
    res[0].size -= 1
    res[-1].size -= 1
    res[0].to -= 1
    res[-1].to -= 1
    for x in res[1:]:
        x.fro -= 1
        x.to -= 1

    # Append alternating:
    # print(res)
    new_res = []
    # all pairs (A0, A1), (A1, A2), ... (An-2, An-1)
    for x, y in zip(res, res[1:]):
        new_res.append(x)
        if x.to != y.fro:
            new_res.append(Alter(y.fro - x.to, x.to, y.fro))
    new_res.append(res[-1])
    return new_res


def other_col(x):
    return 'B' if x == 'W' else 'W'


def alter_col(start, size):
    oth = other_col(start)
    res = []
    for i in range(size):
        if i % 2 == 0:
            res.append(start)
        else: res.append(oth)
    return ''.join(res)


def compute_alter(size, prv_col, nxt_col, k):
    # Every step, size decreases by 2:
    size_after_k = max(0, size - 2 * k)
    assert size % 2 == (1 if prv_col == nxt_col else 0)
    if size_after_k == 0:
        if prv_col == nxt_col:
            return prv_col * size
        # Otherwise it's split evenly in the two colors of prv_col, nxt_col
        else:
            return prv_col * (size // 2) + nxt_col * (size // 2)
    else:
        alter_middle = alter_col(other_col(prv_col), size_after_k)
        return prv_col * k + alter_middle + nxt_col * k


def simulate(splitted, k):
    res = [splitted[0].col * splitted[0].size]
    if len(splitted) == 1: return res
    for i in range(1, len(splitted) - 1):
        prv, curr, nxt = splitted[i - 1], splitted[i], splitted[i + 1]
        if isinstance(curr, Alter):
            assert isinstance(prv, Same) and isinstance(nxt, Same)
            alter_after_change = compute_alter(curr.size, prv.col, nxt.col, k)
            assert len(alter_after_change) == curr.size
            res.append(alter_after_change)
        else:
            res.append(curr.col * curr.size)
    res.append(splitted[-1].col * splitted[-1].size)
    return res


def test(lst, k):
    n = len(lst)
    # look for 2 in a row (there are at least 3:)
    two_in_row = None
    for i, (cur, prv) in enumerate(zip(lst, lst[1:] + lst[0])):
        if cur == prv:
            two_in_row = i
            break
    #print(list(enumerate(zip(lst, lst[1:] + lst[0]))))
    # print(two_in_row)

    if two_in_row is None:
        if k % 2 == 0:
            return lst
        else:
            # flip it:
            return ''.join('B' if x == 'W' else 'W' for x in lst)

    # re-cut it so that start and end never change:
    #   i=_
    # BWBWBBWW
    #   i-^
    # print(lst)
    flip = i
    lst = lst[flip + 1:] + lst[:flip + 1]
    #print("Flipped: ", lst)
    smpl = simpl(lst)
    #print("Parsed: ", smpl)
    before_flip_res = simulate(smpl, k)
    #print("Simulated: ", before_flip_res)
    before_flip_res = ''.join(before_flip_res)
    after_flip = n - (flip + 1)
    #print("First part:", before_flip_res[after_flip:])
    #print("Second part: ", before_flip_res[:after_flip])

    # flip it back:
    return before_flip_res[after_flip:] + before_flip_res[:after_flip]


def sim_slow(lst, k):
    for _ in range(k):
        nxt_lst = [None for _ in range(len(lst))]
        for i, curr in enumerate(lst):
            prv, curr, nxt = lst[i - 1], lst[i], lst[(i + 1) % len(lst)]
            nW = [prv, curr, nxt].count('W')
            nB = [prv, curr, nxt].count('B')
            if nW >= 2:
                nxt_lst[i] = 'W'
            else: nxt_lst[i] = 'B'
        lst = nxt_lst
    return ''.join(lst)


if False:
    import itertools
    for x in itertools.product("BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW"):
        x = ''.join(x)
        for k in range(10):
            if sim_slow(x, k) != test(x, k):
                print(x, k, sim_slow(x, k), test(x, k))
                assert False

#t = int(input())
for _ in range(1):
    _, k = [int(x) for x in input().split()]
    lst = input()
    res = test(lst, k)
    # print("result: ", res)
    # print("\n")
    print(res)

# print(simpl(lst))
