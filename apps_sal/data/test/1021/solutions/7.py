def get(l):
    res = {}
    for i in range(1, n):
        if l[i] - l[i - 1] in res:
            res[l[i] - l[i - 1]] += 1
        else:
            res[l[i] - l[i - 1]] = 1
    return res


(n, a, b) = (int(input()), [int(_) for _ in input().split()], [int(_) for _ in input().split()])
(ma, mb) = (get(a), get(b))
print('Yes' if ma == mb and a[0] == b[0] and (a[-1] == b[-1]) else 'No')
