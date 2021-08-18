
s = input()
n = int(input())
t = [0 for i in range(len(s) * 4)]

bits = dict()
b = 1
for i in range(97, 123):
    bits[chr(i)] = b
    b <<= 1


def bit_repr(a):
    return bits[a]


def popcount(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


def build(A, v, t_left, t_right):

    if t_left == t_right:
        t[v] |= bit_repr(A[t_left])
        return

    left_son = (v << 1) + 1
    right_son = left_son + 1
    t_mid = (t_left + t_right) >> 1

    build(A, left_son, t_left, t_mid)
    build(A, right_son, t_mid + 1, t_right)

    t[v] = t[left_son] | t[right_son]


def _update(v, t_left, t_right, index, val):
    while t_left != t_right:
        t_mid = (t_left + t_right) >> 1
        left_son = (v << 1) + 1
        right_son = left_son + 1
        if index > t_mid:
            t_left = t_mid + 1
            v = right_son
        else:
            t_right = t_mid
            v = left_son
    t[v] = bit_repr(val)
    while v:
        v = (v - 1) >> 1
        left_son = (v << 1) + 1
        right_son = left_son + 1
        t[v] = t[left_son] | t[right_son]


def get_set(v, t_left, t_right, left, right):
    if left > right:
        return 0
    if t_left == left and t_right == right:
        return t[v]
    t_mid = (t_left + t_right) >> 1

    left_son = (v << 1) + 1
    right_son = left_son + 1

    a = get_set(left_son, t_left, t_mid, left, min(right, t_mid))
    b = get_set(right_son, t_mid + 1, t_right, max(left, t_mid + 1), right)

    return a | b


def update(index, val):
    '''Interface for _update function'''
    _update(0, 0, len(s) - 1, index - 1, val)


def count(l, r):
    '''Interface for popcount(get_set())'''
    return popcount(get_set(0, 0, len(s) - 1, l - 1, r - 1))


def process():
    req = iter(input().split())
    token = int(next(req))
    if token - 1:
        l, r = list(map(int, req))
        print(count(l, r))
    else:
        pos = int(next(req))
        sym = next(req)
        update(pos, sym)


build(s, 0, 0, len(s) - 1)

for i in range(n):
    process()
