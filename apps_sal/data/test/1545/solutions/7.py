import sys
from collections import deque


def debug(x, table):
    for (name, val) in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def get_minsp(message, As):
    min_sp = 1
    cur_len = 0
    capa = 0
    for ch in message:
        index = ord(ch) - ord('a')
        if cur_len == 0:
            cur_len += 1
            capa = As[index]
        else:
            capa = min(capa, As[index])
            if cur_len + 1 <= capa:
                cur_len += 1
            else:
                min_sp += 1
                cur_len = 1
                capa = As[index]
    return min_sp


def solve():
    MOD = 10 ** 9 + 7
    n = int(input())
    message = input()
    As = [int(i) for i in input().split()]
    capas = []
    for ch in message:
        i = ord(ch) - ord('a')
        capas.append(As[i])
    deq = deque()
    cur_len = 0
    max_len = 0
    min_sp = 0
    capa = 0
    for (i, capa) in enumerate(capas):
        if not deq:
            deq.append(1)
            cur_len = 1
            max_len = 1
        else:
            limit = capa
            lim_len = capa
            for j in range(1, min(i + 1, capa)):
                if min(limit, capas[i - j]) < j + 1:
                    lim_len = j
                    break
                limit = min(limit, capas[i - j])
            else:
                lim_len = min(i + 1, capa)
            deq.appendleft(sum(deq) % MOD)
            if cur_len + 1 <= lim_len:
                cur_len += 1
                max_len = max(cur_len, max_len)
            else:
                num_del = cur_len + 1 - lim_len
                for j in range(num_del):
                    deq.pop()
                cur_len = lim_len
    min_sp = get_minsp(message, As)
    print(sum(deq) % MOD)
    print(max_len)
    print(min_sp)


def __starting_point():
    solve()


__starting_point()
