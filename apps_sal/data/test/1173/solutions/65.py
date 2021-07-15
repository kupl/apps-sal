from collections import deque
n = int(input())
a_list = []
for i in range(n):
    a_list.append(deque([int(aa) - 1 for aa in input().split()]))
day = 0
battle = 0
for _ in range(n * (n - 1) // 2):
    if battle == n * (n - 1) // 2:
        break
    day += 1
    battle_today = 0
    tomorrow = set([])
    if (day == 1):
        player = set([i for i in range(n)])
    for i in player:
        if len(a_list[i]) == 0:
            continue
        j = a_list[i][0]
        if (i == a_list[j][0]) & (j not in tomorrow) & (len(a_list[j]) > 0) & (i not in tomorrow):
            tomorrow.add(i)
            tomorrow.add(a_list[i][0])
            battle += 1
            battle_today += 1
            a_list[i].popleft()
            a_list[j].popleft()
    player = tomorrow
    if battle_today == 0:
        day = -1
        break
print(day)
