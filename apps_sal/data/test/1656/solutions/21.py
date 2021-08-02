from sys import stdin

s = stdin.readline().strip()
n = len(s)
l = [0 for i in range(n)]
r = [0 for i in range(n)]


def cal(x):
    return (x * (x - 1)) // 2


for i in range(n):
    if i == 0:
        continue
    if s[i] == "v" and s[i - 1] == "v":
        l[i] += 1
    l[i] += l[i - 1]
for i in range(n - 1, -1, -1):
    if i == n - 1:
        continue
    if s[i] == "v" and s[i + 1] == "v":
        r[i] += 1
    r[i] += r[i + 1]
ans = 0
for i in range(n):
    if s[i] == "o":
        ans += l[i] * r[i]
print(ans)
