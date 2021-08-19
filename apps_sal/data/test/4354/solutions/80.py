(n, m) = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(n)]
cd = [list(map(int, input().split())) for j in range(m)]
for i in range(n):
    dis = float('inf')
    ch = 0
    for j in range(m):
        if dis > abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1]):
            dis = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
            ch = j
    print(ch + 1)
