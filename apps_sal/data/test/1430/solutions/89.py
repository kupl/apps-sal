from itertools import groupby

n, k = list(map(int, input().split()))
s = input()

grouped = groupby(s)

res = []

if s[0] == '0':
    res.append(0)

for l, v in grouped:
    res.append((len(list(v))))

if s[len(s) - 1] == '0':
    res.append(0)

now = 0
ans = 0
for i in range(min(len(res), 2 * k + 1)):
    now += res[i]

ans = max(ans, now)

for i in range(2 * k + 1, len(res), 2):
    now -= res[i - 2 * k - 1]
    now -= res[i - 2 * k]

    now += res[i]
    now += res[i + 1]

    ans = max(ans, now)

print(ans)
