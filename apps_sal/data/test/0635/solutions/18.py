def reachable(s, l, r):
    if not r[0]:
        return False
    if r[s]:
        return True
    if not l[s]:
        return False
    return any([arg[0] == 1 and arg[1] == 1 for arg in zip(r[s:], l[s:])])


(n, s) = list(map(int, input().split(' ')))
r = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))
print('YES' if reachable(s - 1, l, r) else 'NO')
