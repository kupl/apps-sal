n, q = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q)]
INF = 10 ** 9

ver = [-1] * (n + 1)
hor = [-1] * (n + 1)
ver[-1] = INF
hor[-1] = INF
ver_base = n - 1
hor_base = n - 1

white = 2 * n - 1
for num, x in query:
    if num == 1:
        if ver[x] == -1:
            white += ver_base
            i = x
            while ver[i] == -1:
                ver[i] = ver_base
                i += 1

        else:
            white += ver[x]

        hor_base = min(hor_base, x - 1)

    else:
        if hor[x] == -1:
            white += hor_base
            i = x
            while hor[i] == -1:
                hor[i] = hor_base
                i += 1

        else:
            white += hor[x]

        ver_base = min(ver_base, x - 1)

stone_sum = (n - 2) * (n - 2) + 2 * n - 1 + q
ans = stone_sum - white
print(ans)
