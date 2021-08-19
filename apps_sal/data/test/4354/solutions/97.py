(n, m) = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    num = 0
    ans = float('inf')
    for j in range(m):
        man = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if man < ans:
            ans = man
            num = j
    print(num + 1)
