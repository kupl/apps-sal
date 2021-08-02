n, m = map(int, input().split())
dic = {}
doll = 0
AB = [list(map(int, input().split())) for _ in range(n)]

AB.sort()

for k, v in AB:
    if v < m:
        doll += k * v
        m -= v
    else:
        doll += k * m
        break
print(doll)
