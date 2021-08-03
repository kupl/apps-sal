s = input()
l = len(s)

d = [[-1, 0, -1] for i in range(26)]
k = [-1 for i in range(26)]


for i in range(l):
    n = ord(s[i]) - 97
    if d[n][0] == -1:
        d[n][0] = i
        d[n][2] = i
    else:
        d[n][1] = max(d[n][1], i - d[n][0])
        d[n][0] = i

ans = l
for i in range(26):
    if d[i][0] != -1:
        k[i] = max(d[i][2], l - d[i][0] - 1, d[i][1] - 1)
    if k[i] > -1:
        ans = min(ans, k[i])

print(ans + 1)
