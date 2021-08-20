def dist(cur, king):
    distance = abs(cur[0] - king[0]) ** 2 + abs(cur[1] - king[1]) ** 2
    direction = ''
    if cur[0] > king[0]:
        direction += 'l'
    elif cur[0] < king[0]:
        direction += 'r'
    if cur[1] > king[1]:
        direction += 'u'
    elif cur[1] < king[1]:
        direction += 'd'
    return (distance, direction)


amount = int(input())
king = input().split()
king = [int(k) for k in king]
all_figurs = {}
figurs = {}
for i in range(amount):
    figura = input().split()
    all_figurs[int(figura[1]), int(figura[2])] = figura[0]
for key in all_figurs.keys():
    if key[0] == king[0] or key[1] == king[1] or abs(king[0] - key[0]) == abs(king[1] - key[1]):
        figurs[key] = all_figurs[key]
nearest = {k: (10 ** 100, '?') for k in ['l', 'lu', 'ld', 'r', 'ru', 'rd', 'u', 'd']}
for key in figurs.keys():
    (distance, direction) = dist(key, king)
    if nearest[direction][0] > distance:
        nearest[direction] = (distance, figurs[key])
is_shah = False
for key in nearest.keys():
    if nearest[key][1] in ['Q', 'B'] and len(key) == 2:
        is_shah = True
        break
    if nearest[key][1] in ['Q', 'R'] and len(key) == 1:
        is_shah = True
        break
if is_shah:
    print('YES')
else:
    print('NO')
