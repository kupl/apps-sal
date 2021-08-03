from functools import lru_cache


def f(n, table):
    s = {"ab"}
    tmp = set()
    for _ in range(n - 2):
        for ss in s:
            for i in range(len(ss) - 1):
                tmp.add(ss[: i + 1] + table[ss[i: i + 2]] + ss[i + 1:])
        s, tmp = tmp, set()
    return len(s)


M = 1_000_000_007


def fib(n):
    ret = [1, 1]
    cur = 1
    for i in range(n):
        ret.append(ret[cur] + ret[cur - 1])
        cur += 1
    return ret[n] % M


def t(n):
    return (2 ** n) % M


ab = "ab"
n = int(input().strip())
table = []
for _ in range(4):
    table.append(input().strip().lower())
table = dict(list(zip(["aa", "ab", "ba", "bb"], table)))

fn = f(5, table)

if fn == 1:
    print((1))
elif fn == 3:
    print((fib(n - 2)))
else:
    if n == 2:
        print((1))
    else:
        print((t(n - 3)))
