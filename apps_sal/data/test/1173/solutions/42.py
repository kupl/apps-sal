from collections import deque

n = int(input())
matches = []
for _ in range(n):
    matches.append(list([int(x) - 1 for x in input().split()]))

q = deque(list(range(n)))

days = [0] * n  # 各選手の現在の日付

while q:
    x = q.popleft()  # 試合する人
    if len(matches[x]) == 0:  # 試合が全て終わってる?
        continue
    y = matches[x][0]  # xの次の対戦相手
    if matches[y][0] == x:
        day = max(days[x], days[y]) + 1
        days[x] = day
        days[y] = day
        q.append(x)
        q.append(y)
        _ = matches[x].pop(0)
        _ = matches[y].pop(0)

if not any(matches):  # 全ての試合をしょうか
    print((max(days)))
else:
    print((-1))
