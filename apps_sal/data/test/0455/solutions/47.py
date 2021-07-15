###############################################################################

from sys import stdout
from bisect import bisect_left as binl
from copy import copy, deepcopy

def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def modadd(x, y):
    nonlocal mod
    return (x + y) % mod


def modmlt(x, y):
    nonlocal mod
    return (x * y) % mod


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


def get_divisors(x):
    retlist = []
    for i in range(1, int(x**0.5) + 3):
        if x % i == 0:
            retlist.append(i)
            retlist.append(x // i)
    return retlist


def make_linklist(xylist):
    linklist = {}
    for a, b in xylist:
        linklist.setdefault(a, [])
        linklist.setdefault(b, [])
        linklist[a].append(b)
        linklist[b].append(a)
    return linklist


def calc_longest_distance(linklist, v=1):
    distance_list = {}
    distance_count = 0
    distance = 0
    vlist_previous = []
    vlist = [v]
    nodecount = len(linklist)

    while distance_count < nodecount:
        vlist_next = []
        for v in vlist:
            distance_list[v] = distance
            distance_count += 1
            vlist_next.extend(linklist[v])
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous = vlist
        vlist = list(set(vlist_next) - set(vlist_to_del))

    max_distance = -1
    max_v = None
    for v, distance in list(distance_list.items()):
        if distance > max_distance:
            max_distance = distance
            max_v = v

    return (max_distance, max_v)


def calc_tree_diameter(linklist, v=1):
    _, u = calc_longest_distance(linklist, v)
    distance, _ = calc_longest_distance(linklist, u)
    return distance


###############################################################################


def main():
    n = intin()
    xylist = intinl(n)

    even_odd = None
    uvlist = []

    for x, y in xylist:
        tmp_even_odd = (x + y) % 2

        if even_odd is None:
            even_odd = tmp_even_odd

        if even_odd != tmp_even_odd:
            print((-1))
            return

        uvlist.append((x + y, x - y))

    m = 33 if even_odd else 34

    print(m)
    dlist = [str(2**i) for i in reversed(list(range(0, 33)))]
    if not even_odd:
        dlist.append('1')
    print((' '.join(dlist)))

    for u, v in uvlist:

        if not even_odd:
            u += 1
            v += 1
        line = ''

        if u >= 0 and v >= 0:
            line += 'R'
        if u >= 0 and v < 0:
            line += 'U'
        if u < 0 and v >= 0:
            line += 'D'
        if u < 0 and v < 0:
            line += 'L'

        for i in reversed(list(range(1, 33))):
            u_bit = (u >> i) & 1
            v_bit = (v >> i) & 1
            if u_bit and v_bit:
                line += 'R'
            if u_bit and not v_bit:
                line += 'U'
            if not u_bit and v_bit:
                line += 'D'
            if not u_bit and not v_bit:
                line += 'L'

        if not even_odd:
            line += 'L'

        print(line)


def __starting_point():
    main()

__starting_point()
