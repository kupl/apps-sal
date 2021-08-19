(n, k, m, t) = list(map(int, input().split(' ')))
for _ in range(t):
    (op, pos) = list(map(int, input().split(' ')))
    if op == 1:
        if k >= pos:
            k += 1
        n += 1
    elif k > pos:
        n -= pos
        k -= pos
    else:
        n = pos
    print(n, k)
