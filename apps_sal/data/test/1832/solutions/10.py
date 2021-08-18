import sys


def solve(lens):
    base = ord('a')
    wlen = max(lens) + 2
    last = ['a'] * wlen
    word_list = [''.join(last)]
    for l in lens:
        last[l] = chr(base + (ord(last[l]) - ord('a') + 1) % 26)
        word_list.append(''.join(last))
    return word_list


def __starting_point():
    IN = [x.strip() for x in sys.stdin.readlines()]

    T = int(IN[0])
    cur = 1
    for ti in range(T):
        a = int(IN[cur])
        lens = [int(x) for x in IN[cur + 1].split(' ')]
        res = solve(lens)
        for w in res:
            print(w)
        cur += 2


__starting_point()
