(n, m) = map(int, input().split())
ka = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(m + 1):
    suki = 0
    for j in range(n):
        if i in ka[j][1:]:
            suki += 1
    if suki == n:
        cnt += 1
print(cnt)
