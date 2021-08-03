n, q = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q)]
INF = 10 ** 9

keys = ["verticle", "horizion"]

become_white = {key: [-1] * (n + 1) for key in keys}
for key in keys:
    become_white[key][-1] = INF
base = {key: n - 1 for key in keys}

white = 2 * n - 1
for num, x in query:
    if num == 1:
        i, j = keys
    else:
        j, i = keys

    if become_white[i][x] == -1:
        white += base[i]
        k = x
        while become_white[i][k] == -1:
            become_white[i][k] = base[i]
            k += 1
    else:
        white += become_white[i][x]

    base[j] = min(base[j], x - 1)

stone_sum = (n - 2) * (n - 2) + 2 * n - 1 + q
ans = stone_sum - white
print(ans)
