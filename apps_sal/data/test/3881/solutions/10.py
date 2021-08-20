import collections
(n, q) = [int(x) for x in input().split()]
g = dict()
for i in range(q):
    (to, f) = input().split()
    if f in g:
        g[f].append(to)
    else:
        g[f] = [to]
counts = dict()


def count(s):
    if s in counts:
        return counts[s]
    if len(s) == n:
        counts[s] = 1
        return 1
    if len(s) > n:
        return 0
    c = s[0]
    cnt = 0
    if not c in g:
        return 0
    suff = s[1:]
    for j in g[c]:
        new_s = j + suff
        cnt += count(new_s)
    counts[s] = cnt
    return cnt


print(count('a'))
