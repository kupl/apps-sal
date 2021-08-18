import queue
import copy
q = queue.Queue()
h, w = list(map(int, input().split()))
a = [list('
a=[['
a1=copy.deepcopy(a)
ans=[]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        a=copy.deepcopy(a1)
        if a[i][j] == '
            continue
        q.put([i, j, 0])
        while not q.empty():
            now=q.get()

            if a[now[0]][now[1]] == '.':
                ans.append(now[2])
                a[now[0]][now[1]]= '
            else:
                continue

            if a[now[0] + 1][now[1]] != '
                q.put([now[0] + 1, now[1], now[2] + 1])
            if a[now[0] - 1][now[1]] != '
                q.put([now[0] - 1, now[1], now[2] + 1])
            if a[now[0]][now[1] + 1] != '
                q.put([now[0], now[1] + 1, now[2] + 1])
            if a[now[0]][now[1] - 1] != '
                q.put([now[0], now[1] - 1, now[2] + 1])
        a1[i][j] == '
print((max(ans)))
