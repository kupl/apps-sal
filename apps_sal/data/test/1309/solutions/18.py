def readln(): return list(map(int, input().rstrip().split()))


def cal(dt):
    rs = 0
    for i in range(len(dt) // 2):
        rs += abs(dt[2 * i] - dt[2 * i + 1])
    return rs


n = int(input())
data = list(readln())
data.sort()

minw = 500000

for i in range(0, 2 * n - 1):
    for j in range(i + 1, 2 * n):
        dt = list(data)
        dt.pop(max(i, j))
        dt.pop(min(i, j))
        rs = cal(dt)
        if rs < minw:
            minw = rs

print(minw)
