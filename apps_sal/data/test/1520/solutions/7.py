import os
from io import BytesIO
from collections import namedtuple
Parsed = namedtuple('Parsed', 'type p pl s sl')
(D, U) = (0, 1)


def parse(s):
    (pc, sc) = (0, 0)
    for c in s:
        if c != s[0]:
            break
        pc += 1
    for c in reversed(s):
        if c != s[-1]:
            break
        sc += 1
    if s[0] == s[-1] and pc == sc == len(s):
        tp = U
    else:
        tp = D
    return Parsed(tp, s[0], pc, s[-1], sc)


def max_conti_len(s, target):
    mx = 0
    cur = 0
    for c in s:
        if c == target:
            cur += 1
            mx = max(mx, cur)
        else:
            cur = 0
    return mx


def len_mul(nl, ol):
    return ol * nl + ol + nl


def solve(n, ss):
    s = ss.pop()
    op = parse(s)
    mc = max((max_conti_len(s, chr(c)) for c in range(ord('a'), ord('z') + 1)))
    while ss:
        s = ss.pop()
        np = parse(s)
        if np.type == U and op.type == U:
            if np.p == op.p:
                nl = len_mul(np.pl, op.pl)
                op = Parsed(U, op.p, nl, op.s, nl)
            else:
                op = Parsed(D, op.p, op.pl, op.s, op.sl)
            mc = max(mc, op.pl)
        elif np.type == D and op.type == U:
            npl = len_mul(np.pl, op.pl) if np.p == op.p else op.pl
            nsl = len_mul(np.sl, op.sl) if np.s == op.s else op.sl
            mx = max_conti_len(s, op.s)
            mc = max(mc, len_mul(mx, op.pl))
            op = Parsed(D, op.p, npl, op.s, nsl)
        elif op.type == D:
            if op.p == op.s:
                mp = op.pl + op.sl + 1 if op.p in s else op.pl
                ms = op.sl
            else:
                mp = op.pl + 1 if op.p in s else op.pl
                ms = op.sl + 1 if op.s in s else op.sl
            mc = max(mc, mp, ms)
    print(mc)


def solve_from_stdin():
    n = int(input())
    ss = []
    for _ in range(n):
        ss.append(input())
    solve(n, ss)


solve_from_stdin()
