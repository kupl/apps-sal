import sys
import math
import queue
MOD = 10 ** 9 + 7


def getBin(x):
    num = [-1 for i in range(32)]
    for i in range(1, 33):
        num[-i] = x & 1
        x = x >> 1
    return num


t = [-1, -1]


def add(x, trie, i):
    if i == len(x):
        return
    if trie[x[i]] == -1:
        trie[x[i]] = [-1, -1]
    add(x, trie[x[i]], i + 1)


def query(x, trie, i, ans):
    if i == len(x):
        return ans
    if x[i] == 1:
        if trie[0] == -1:
            return query(x, trie[1], i + 1, ans << 1)
        else:
            return query(x, trie[0], i + 1, (ans << 1) + 1)
    elif trie[1] == -1:
        return query(x, trie[0], i + 1, ans << 1)
    else:
        return query(x, trie[1], i + 1, (ans << 1) + 1)


def delete(x, trie, i):
    if i == len(x):
        return
    delete(x, trie[x[i]], i + 1)
    if trie[x[i]] == [-1, -1]:
        trie[x[i]] = -1


n = int(input())
add(getBin(0), t, 0)
f = {0: 1}
for _ in range(n):
    (q, x) = input().split()
    x = int(x)
    if q == '+':
        if x in f:
            f[x] += 1
        else:
            f[x] = 1
            add(getBin(x), t, 0)
    elif q == '?':
        print(query(getBin(x), t, 0, 0))
    elif f[x] == 1:
        del f[x]
        delete(getBin(x), t, 0)
    else:
        f[x] -= 1
