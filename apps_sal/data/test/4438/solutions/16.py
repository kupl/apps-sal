import sys


def cal(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def cmp(a, b):
    if a[0] != b[0]:
        return a[0] < b[0]
    return a[1] > b[1]


rd = sys.stdin.readlines()
n = int(rd[0])
data = {}
for _ in range(0, n):
    x, y = map(int, rd[_ + 1].split())
    if max(x, y) not in data:
        data[max(x, y)] = []
    data[max(x, y)].append((x, y))
dp1, dp2 = 0, 0
pre1, pre2 = (0, 0), (0, 0)
for i in sorted(list(data.keys())):
    now1, now2 = data[i][0], data[i][0]
    for x in data[i]:
        if cmp(now1, x):
            now1 = x
        if cmp(x, now2):
            now2 = x
    dp1, dp2 = min(dp1 + cal(pre1, now2) + cal(now2, now1), dp2 + cal(pre2, now2) + cal(now2, now1)), min(dp1 + cal(pre1, now1) + cal(now1, now2), dp2 + cal(pre2, now1) + cal(now1, now2))
    pre1, pre2 = now1, now2
print(min(dp1, dp2))
