from collections import deque
(N, D, A) = map(int, input().split())
monster = []
for k in range(N):
    monster.append(list(map(int, input().split())))
monster.sort(key=lambda x: x[0])
for k in range(N):
    monster[k][1] = int((monster[k][1] - 0.1) // A + 1)
ans = 0
monster = deque(monster)
final = monster[-1][0]
ruiseki = 0
minuslist = deque()
while len(monster) > 0:
    while len(minuslist) > 0:
        if monster[0][0] >= minuslist[0][0]:
            ruiseki -= minuslist[0][1]
            minuslist.popleft()
        else:
            break
    if ruiseki < monster[0][1]:
        ans += monster[0][1] - ruiseki
        if monster[0][0] + 2 * D + 1 <= final:
            minuslist.append([monster[0][0] + 2 * D + 1, monster[0][1] - ruiseki])
        ruiseki = monster[0][1]
    monster.popleft()
print(ans)
