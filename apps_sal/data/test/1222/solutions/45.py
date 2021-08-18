from collections import deque
k = int(input())
num = []


def dfs(lun):
    num.append(lun)
    if lun > 3234566667:
        return
    now = lun % 10
    for i in [-1, 0, 1]:
        if 0 <= now + i <= 9:
            dfs(lun * 10 + now + i)


for i in range(1, 10):
    dfs(i)
num.sort()
print((num[k - 1]))
