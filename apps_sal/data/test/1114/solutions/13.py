from collections import Counter


def solve(n, m, f, b):
    d1 = Counter(f)
    d2 = Counter(b)
    (flag1, flag2) = (True, False)
    for (k, v) in d2.items():
        if k not in d1:
            flag1 = False
            break
    if not flag1:
        print('Impossible')
        return
    for (k, v) in d2.items():
        if d1[k] > 1:
            flag2 = True
            break
    if flag2:
        print('Ambiguity')
        return
    d = {k: pos for (pos, k) in enumerate(f, start=1)}
    print('Possible')
    for value in b:
        print(d[value], end=' ')


(n, m) = map(int, input().split())
f = list(map(int, input().split()))
b = list(map(int, input().split()))
solve(n, m, f, b)
