n, m = map(int, input().split())

swl = [list(map(int, input().split())) for _ in range(m)]
pl = list(map(int, input().split()))
ans = 0
for i in range(2**n):
    sw = [0] * n
    light_cnt = 0
    for j in range(n):
        if (i >> j) & 1:
            sw[j] += 1
    for j in range(m):
        wl = swl[j][1:]
        sw_cnt = 0
        for wi in wl:
            if sw[wi - 1] == 1:
                sw_cnt += 1
        if sw_cnt % 2 == pl[j]:
            light_cnt += 1
    if light_cnt == m:
        ans += 1

print(ans)
