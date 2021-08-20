from sys import stdin, stdout
n = int(stdin.readline())
s = stdin.readline().strip()
cnt = [[0, 0] for i in range(n)]
cnt[0][1] = int(s[0])
cnt[0][0] = 1 - int(s[0])
for i in range(1, n):
    cnt[i][1] += cnt[i - 1][1] + int(s[i])
    cnt[i][0] = i + 1 - cnt[i][1]
cnt.append([0, 0])
ans = 0
for i in range(n):
    value = int(s[i])
    current = i + ans
    while current < n:
        if max(cnt[current][1] - cnt[i - 1][1], cnt[current][0] - cnt[i - 1][0]) != min(cnt[current][1] - cnt[i - 1][1], cnt[current][0] - cnt[i - 1][0]):
            current += max(cnt[current][1] - cnt[i - 1][1], cnt[current][0] - cnt[i - 1][0]) - min(cnt[current][1] - cnt[i - 1][1], cnt[current][0] - cnt[i - 1][0])
        else:
            ans = max(ans, current - i + 1)
            current += 1
stdout.write(str(ans))
