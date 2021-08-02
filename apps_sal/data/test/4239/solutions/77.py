N = int(input())
kouho = [1]
for i in range(1, 100):
    t = 6 ** i
    if t <= 10 ** 5:
        kouho.append(t)
    else:
        break
for i in range(1, 100):
    t = 9 ** i
    if t <= 10 ** 5:
        kouho.append(t)
    else:
        break
# print(kouho)

kouho.sort(reverse=True)
kouho_cnt = len(kouho)
INF = 10 ** 9
dp = [INF] * ((10 ** 5) + 1)
dp[0] = 0
for i in range(1, N + 1):
    for k in kouho:
        if i - k >= 0:
            dp[i] = min(dp[i], dp[i - k] + 1)
# print(dp)
print((dp[N]))
# cur = 0
# ans = 0
# while N > 0:
#     if N >= kouho[cur]:
#         N -= kouho[cur]
#         ans += 1
#     else:
#         cur += 1
# print(ans)
