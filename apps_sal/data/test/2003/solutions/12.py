from collections import defaultdict
import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.cnt = 0
        self.next = [None] * 2


trie = Trie()


def add(x):
    mask = 1 << 32
    cur = trie
    while mask:
        if mask & x:
            if not cur.next[1]:
                cur.next[1] = Trie()
            cur = cur.next[1]
        else:
            if not cur.next[0]:
                cur.next[0] = Trie()
            cur = cur.next[0]
        cur.cnt += 1
        mask >>= 1


def remove(x):
    mask = 1 << 32
    cur = trie
    while mask:
        if mask & x:
            cur = cur.next[1]
        else:
            cur = cur.next[0]
        cur.cnt -= 1
        mask >>= 1


def query(x):
    mask = 1 << 32
    cur = trie
    ret = 0
    while mask:
        if mask & x:
            if cur.next[0] and cur.next[0].cnt > 0:
                cur = cur.next[0]
                ret += mask
            else:
                cur = cur.next[1]
        else:
            if cur.next[1] and cur.next[1].cnt > 0:
                cur = cur.next[1]
                ret += mask
            else:
                cur = cur.next[0]
        mask >>= 1
    return ret


add(0)
q = int(input())
for _ in range(q):
    comm, x = input().split()
    x = int(x)
    if comm == '+':
        add(x)
    elif comm == '-':
        remove(x)
    else:
        print(query(x))
