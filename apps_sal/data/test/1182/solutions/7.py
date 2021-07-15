def check(x1, y1, x2, y2):
    nonlocal dp
    cnt = 0
    for i in range(x2, x1 + 1):
        for j in range(y2, y1 + 1):
            cnt += dp[i][j]
    return cnt


#n = int(input())
r, c, n, k = list(map(int, input().split()))
#s = list(map(int, input().split()))
dp = [[0] * c for i in range(r)]
for i in range(n):
    a, b = list(map(int, input().split()))
    dp[a - 1][b - 1] = 1
answer = 0
for x1 in range(r):
    for y1 in range(c):
        for x2 in range(x1 + 1):
            for y2 in range(y1 + 1):
                cnt = check(x1, y1, x2, y2)
                #print(cnt, x1, y1, x2, y2)
                if cnt >= k:
                    answer += 1
print(answer)

