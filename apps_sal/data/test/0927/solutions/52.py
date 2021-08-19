import sys
readline = sys.stdin.readline
(N, M) = map(int, readline().split())
A = set(list(map(int, readline().split())))
dic = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
candi = [[], [], [1], [7], [4], [2, 3, 5], [6, 9], [8]]
if 2 in A and 3 in A:
    A.remove(2)
if 2 in A and 5 in A:
    A.remove(2)
if 3 in A and 5 in A:
    A.remove(3)
if 6 in A and 9 in A:
    A.remove(6)
for i in range(len(candi)):
    for j in range(len(candi[i]) - 1, -1, -1):
        if candi[i][j] not in A:
            del candi[i][j]
dp = [-1] * (N + 1)
ans = [''] * (N + 1)
dp[0] = 0


def to_num(x):
    return int(''.join(sorted(x, reverse=True)))


for i in range(len(candi)):
    if not candi[i]:
        continue
    num = str(candi[i][0])
    for j in range(len(dp)):
        if dp[j] == -1:
            continue
        if j + i > N:
            continue
        if dp[j + i] < dp[j] + 1:
            dp[j + i] = dp[j] + 1
            ans[j + i] = ans[j] + num
        elif dp[j + i] == dp[j] + 1:
            if to_num(ans[j + i]) < to_num(ans[j] + num):
                ans[j + i] = ans[j] + num
print(to_num(ans[N]))
