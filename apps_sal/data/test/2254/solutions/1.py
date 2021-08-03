n = int(input())

cnt = [[0 for _ in range(n + 1)] for _ in range(2)]

b = [bin(_).count('1') for _ in list(map(int, input().split()))]

res = 0

suf_sum = 0

cnt[0][n] = 1

for i in range(n)[::-1]:
    _sum, mx = 0, 0
    lst_j = i
    add = 0

    for j in range(i, min(n, i + 65)):
        _sum += b[j]

        mx = max(mx, b[j])

        if mx > _sum - mx and _sum % 2 == 0:
            add -= 1

        lst_j = j

    suf_sum += b[i]
    add += cnt[suf_sum & 1][i + 1]
    res += add

    cnt[0][i] = cnt[0][i + 1]
    cnt[1][i] = cnt[1][i + 1]

    if suf_sum & 1:
        cnt[1][i] += 1
    else:
        cnt[0][i] += 1

print(res)
