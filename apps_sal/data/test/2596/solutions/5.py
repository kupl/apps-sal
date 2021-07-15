n, k, m, t = list(map(int, input().split(' ')))

# n = nb univ
# k = doc pos
# m = max nb univ

for _ in range(t):
    op, pos = list(map(int, input().split(' ')))
    if op == 1:
        if k >= pos:
            k += 1
        n += 1
    else:
        if k > pos:
            n -= pos
            k -= pos
        else:
            n = pos

    print(n, k)

