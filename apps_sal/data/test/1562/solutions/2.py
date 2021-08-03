bn = 0
ar = []


def binSearchMax(number):
    last = bn
    first = 0
    mid = (last + first) // 2
    while(last >= first):
        if(ar[mid] < number):
            first = mid + 1
        elif(ar[mid] > number):
            last = mid - 1
        else:
            return mid
        mid = (last + first) // 2
    if (ar[last] == number):
        return last
    return first


n, m, k, q = list(map(int, input().split()))
mmn = [[m, -1] for i in range(n)]
maxn = 0
for i in range(k):
    r, c = list(map(int, input().split()))
    r -= 1
    mmn[r][0] = min(mmn[r][0], c)
    mmn[r][1] = max(mmn[r][1], c)
    maxn = max(maxn, r)
if mmn[0][1] == -1:
    mmn[0][1] = 1
mmn[0][0] = 1
bi = list(map(int, input().split()))
bi += [-1000000000, 10000000000, -1000000000, 10000000000, 10000000000]
bi.sort()
ar = bi
bn = q + 3
dp = [[0, 0] for i in range(n)]

dp[0][1] = mmn[0][1] - mmn[0][0]
dp[0][0] = dp[0][1] * 2
z = 0
for i in range(1, n):
    if mmn[i][1] == -1:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        continue
    p1 = binSearchMax(mmn[z][0])
    p2 = bi[p1 - 1]
    p1 = bi[p1]
    p3 = binSearchMax(mmn[z][1])
    p4 = bi[p3 - 1]
    p3 = bi[p3]
    num1 = abs(p1 - mmn[i][1]) + abs(p1 - mmn[z][0]) + dp[z][0]
    num2 = abs(p2 - mmn[i][1]) + abs(p2 - mmn[z][0]) + dp[z][0]
    num3 = abs(p3 - mmn[i][1]) + abs(p3 - mmn[z][1]) + dp[z][1]
    num4 = abs(p4 - mmn[i][1]) + abs(p4 - mmn[z][1]) + dp[z][1]
    dp[i][0] = min(min(num1, num2), min(num3, num4)) + mmn[i][1] - mmn[i][0]
    num1 = abs(p1 - mmn[i][0]) + abs(p1 - mmn[z][0]) + dp[z][0]
    num2 = abs(p2 - mmn[i][0]) + abs(p2 - mmn[z][0]) + dp[z][0]
    num3 = abs(p3 - mmn[i][0]) + abs(p3 - mmn[z][1]) + dp[z][1]
    num4 = abs(p4 - mmn[i][0]) + abs(p4 - mmn[z][1]) + dp[z][1]
    dp[i][1] = min(min(num1, num2), min(num3, num4)) + mmn[i][1] - mmn[i][0]
    z = i
print(min(dp[-1]) + maxn)
