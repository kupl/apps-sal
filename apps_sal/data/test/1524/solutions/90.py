s = str(input())
s = list(s)
n = len(s)
point = [0] * n
cnt = 1
for i in range(n - 1):
    if s[i] == 'R' and s[i + 1] == 'L':
        point[i] = cnt
        cnt = 1
    elif s[i] == 'R':
        cnt += 1
for i in reversed(range(1, n)):
    if s[i] == 'L' and s[i - 1] == 'R':
        point[i] = cnt
        cnt = 1
    elif s[i] == 'L':
        cnt += 1
ans = [0] * n
for i in range(n - 1):
    if point[i] != 0 and point[i + 1] != 0:
        ans[i] += (point[i] + 1) // 2 + point[i + 1] // 2
        ans[i + 1] += (point[i + 1] + 1) // 2 + point[i] // 2
        point[i + 1] = 0
for i in range(n):
    print(ans[i], end=' ')
