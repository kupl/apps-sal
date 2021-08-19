"""
Created on Sat Mar 21 00:34:22 2015

@author: NEC-PCuser
"""


def solve(n, S, T):
    st = dict()
    ts = dict()
    s = dict()
    t = dict()
    dist = 0
    for (i, (si, ti)) in enumerate(zip(S, T), 1):
        if si != ti:
            st[si, ti] = i
            ts[ti, si] = i
            s[si] = i
            t[ti] = i
            dist += 1
    for (key, i) in st.items():
        if key in ts:
            j = ts[key]
            return (dist - 2, min(i, j), max(i, j))
    for (si, i) in s.items():
        if si in t:
            j = t[si]
            return (dist - 1, min(i, j), max(i, j))
    return (dist, -1, -1)


n = int(input())
S = input()
T = input()
(dist, i, j) = solve(n, S, T)
print(dist)
print(i, j)
