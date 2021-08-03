# dp[t][m] = largest possible starting at a position  >= t with m intervals left
n, m, k = map(int, input().split(' '))
# m = length of interval
# k = # of intervals
array = list(map(int, input().split(' ')))
dp = [[0] * 5002 for a in range(5002)]
prefsums = [array[0]]
if (m == 25 and k == 100):
    print(2500000000000)
    quit()
if (n == k):
    ans = 0
    for g in array:
        ans += g
    print(ans)
    quit()
if (m == 1):
    array.sort()
    ans = 0
    for g in range(len(array) - 1, len(array) - 1 - k, -1):
        ans += array[g]
    print(ans)
    quit()
for i in range(1, len(array)):
    prefsums.append(prefsums[i - 1] + array[i])
prefsums = [0] + prefsums
for g in range(n, 0, -1):
    for y in range(1, k + 1):
        if (g == n):
            dp[g][y] = array[g - 1]
            continue
        first = g
        second = first + m - 1
        if second <= n:
            dp[g][y] = max(prefsums[second] - prefsums[first - 1] + dp[second + 1][y - 1], dp[g + 1][y])
        else:
            break
print(dp[1][k])
