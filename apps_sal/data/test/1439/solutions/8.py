n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
if n > m:
    print("YES")
else:
    d = [{}, {}]
    cur = 0
    for x in l:
        for y in list(d[cur].keys()):
            d[1 - cur][y] = 1
            d[1 - cur][(y + x) % m] = 1
        cur = 1 - cur
        d[cur][x % m] = 1
        if d[cur].get(0, 0):
            break
    print("YES" if d[cur].get(0, 0) else "NO")
