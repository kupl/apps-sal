import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
d = dict()
need = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(m):
    if need[a[i]] not in d:
        d[need[a[i]]] = a[i]
    elif a[i] > d[need[a[i]]]:
        d[need[a[i]]] = a[i]
d = list(d.items())
d.sort()
m = len(d)
dp = [[-1] * 10 for _ in range(n + 1)]
dp[0] = [0] * 10
for i in range(n + 1):
    for j in range(m):
        if i - d[j][0] >= 0 and dp[i - d[j][0]][0] != -1:
            if dp[i][0] == dp[i - d[j][0]][0] + 1:
                ok = False
                for k in reversed(list(range(1, 10))):
                    if k == d[j][1]:
                        if dp[i][k] < dp[i - d[j][0]][k] + 1:
                            ok = True
                            break
                        if dp[i][k] > dp[i - d[j][0]][k] + 1:
                            break
                    else:
                        if dp[i][k] < dp[i - d[j][0]][k]:
                            ok = True
                            break
                        if dp[i][k] > dp[i - d[j][0]][k]:
                            break
                if ok:
                    for k in range(10):
                        dp[i][k] = dp[i - d[j][0]][k]
                    dp[i][d[j][1]] += 1
                    dp[i][0] += 1
            elif dp[i][0] < dp[i - d[j][0]][0] + 1:
                for k in range(10):
                    dp[i][k] = dp[i - d[j][0]][k]
                dp[i][d[j][1]] += 1
                dp[i][0] += 1
ans = str()
for i in reversed(list(range(1, 10))):
    ans += str(i) * dp[-1][i]
print(ans)
