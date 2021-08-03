import sys


def input():
    return sys.stdin.readline().strip()


def solve():
    N = int(input())
    inc_chunks = []
    dec_chunks = []
    for _ in range(N):
        depth = 0
        level = 0
        for c in input():
            if c == '(':
                level += 1
            else:
                level -= 1
                depth = min(depth, level)
        if level > 0:
            inc_chunks.append((depth, level))
        else:
            dec_chunks.append((depth - level, -level))

    inc_chunks.sort(reverse=True)
    dec_chunks.sort(reverse=True)
    inc_level = 0
    for depth, level in inc_chunks:
        if inc_level + depth < 0:
            return 'No'
        inc_level += level
    dec_level = 0
    for depth, level in dec_chunks:
        if dec_level + depth < 0:
            return 'No'
        dec_level += level
    if inc_level != dec_level:
        return 'No'
    return 'Yes'


print((solve()))
