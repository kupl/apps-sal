from collections import deque
k = int(input())
D = deque()
for i in range(1, 10):
    D.append(i)


def dfs(d, val, al):
    al.append(val)
    if d == 10:
        return
    r = val % 10
    for i in range(-1, 2):
        if 0 <= r + i <= 9:
            dfs(d + 1, val * 10 + r + i, al)


al = list()
for i in range(1, 10):
    dfs(1, i, al)
al.sort()
print(al[k - 1])
