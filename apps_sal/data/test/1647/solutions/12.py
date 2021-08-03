from collections import defaultdict
from queue import Queue

IS_WAY_CACHE = set()


def read_nums():
    return [int(x) for x in input().split()]


def is_way(char_map, ch1, ch2):
    nonlocal IS_WAY_CACHE
    q = Queue()
    q.put(ch1)
    visited = {ch1}
    while not q.empty():
        cur_node = q.get()
        if cur_node == ch2:
            return True
        visited.add(cur_node)
        neighbours = char_map[cur_node]
        for n in neighbours:
            IS_WAY_CACHE.add((ch1, n))
            if n not in visited:
                q.put(n)
    return False


def is_way_cache(ch1, ch2):
    return (ch1, ch2) in IS_WAY_CACHE


def main():
    input()
    one, two = input(), input()
    char_map = defaultdict(set)
    res = []
    for ch1, ch2 in zip(one, two):
        if ch1 == ch2:
            continue
        if is_way_cache(ch1, ch2):
            continue
        if is_way_cache(ch2, ch1):
            continue
        if is_way(char_map, ch1, ch2):
            continue
        if is_way(char_map, ch2, ch1):
            continue
        res.append((ch1, ch2))
        char_map[ch1].add(ch2)
        char_map[ch2].add(ch1)

    print(len(res))
    for ch1, ch2 in res:
        print(ch1, ch2)


def __starting_point():
    main()


__starting_point()
