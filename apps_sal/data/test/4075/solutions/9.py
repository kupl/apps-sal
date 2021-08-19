n, m = map(int, input().split())
bulbbit = [0] * m  # 電球とつながっているSWをbit表現
for i in range(m):
    tmp = list(map(int, input().split()))
    for j in range(1, tmp[0] + 1):
        bulbbit[i] |= 1 << (tmp[j] - 1)
p = list(map(int, input().split()))

ans = 0
for s in range(1 << n):
    cnt = 0
    for i in range(m):
        swon = 0
        for j in range(n):
            if s >> j & 1 and bulbbit[i] >> j & 1:
                swon += 1
        if swon % 2 == p[i]:
            cnt += 1
    if cnt == m:
        ans += 1
print(ans)
