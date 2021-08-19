s = input()
mod = 10 ** 9 + 7
retnum = {'?': 0, 'A': 1, 'B': 2, 'C': 3}
count = [[0 for i in range(len(s))] for j in range(4)]
for i in range(len(s)):
    for j in range(4):
        if retnum[s[i]] == j:
            count[j][i] = count[j][i - 1] + 1
        else:
            count[j][i] = count[j][i - 1]
ans = 0
g = [1] * 100002
for i in range(1, 100002):
    g[i] = g[i - 1] * 3
    g[i] %= mod
for i in range(1, len(s) - 1):
    if s[i] == 'B' or s[i] == '?':
        ans += (g[max(0, count[0][i - 1] - 1)] * count[0][i - 1] + g[count[0][i - 1]] * count[1][i - 1]) * (g[max(0, count[0][-1] - count[0][i] - 1)] * (count[0][-1] - count[0][i]) + g[count[0][-1] - count[0][i]] * (count[3][-1] - count[3][i]))
        ans %= mod
print(ans)
