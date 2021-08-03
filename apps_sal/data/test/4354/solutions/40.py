n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    ans = -1
    num = 10**10
    for j in range(m):
        cnt = abs(a[i][0] - b[j][0]) + abs(a[i][1] - b[j][1])
        if cnt < num:
            ans = j + 1
            num = cnt
    print(ans)
