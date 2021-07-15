import heapq


n, k = [int(i) for i in input().split(' ')]

stus = [int(i) for i in input().split(' ')]
ss = sorted(list(enumerate(stus)), key=lambda x: -x[1])
nb = [[i - 1, i + 1] for i in range(n)]
ssid = 0

res = [-1] * n
turn = 0
count = 0
for idx, val in ss:
    if res[idx] != -1:
        continue
    res[idx] = turn % 2 + 1
    left, right = nb[idx]
    for i in range(k):
        if right < n and res[right] == -1:
            res[right] = turn % 2 + 1
            nb[idx][1] = nb[right][1]
            right = nb[right][1]

        if left >= 0 and res[left] == -1:
            res[left] = turn % 2 + 1
            nb[idx][0] = nb[left][0]
            left = nb[left][0]
        if nb[idx][1] < n:
            nb[nb[idx][1]][0] = nb[idx][0]
        if nb[idx][0] >= 0:
            nb[nb[idx][0]][1] = nb[idx][1]
    turn += 1
print(''.join([str(i) for i in res]))

