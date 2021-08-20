def compute(array):
    ggg = 0
    ddd = 0
    fff = 0
    for elem in array:
        if elem[1] == 'f':
            fff += 1
        if elem[1] == 'd':
            ddd += 1
        if elem[1] == 'g':
            ggg += 1
    return (ggg, ddd, fff)


(g, d, f) = list(map(int, input().split()))
gg = list(map(int, input().split()))
dd = list(map(int, input().split()))
ff = list(map(int, input().split()))
players = []
for elem in gg:
    players.append((elem, 'g'))
for elem in dd:
    players.append((elem, 'd'))
for elem in ff:
    players.append((elem, 'f'))
players = sorted(players)
count = 0
left = 0
right = 0
while players[right][0] / players[left][0] <= 2:
    right += 1
    if right == len(players):
        break
right -= 1
(a, b, c) = compute(players[left:right + 1])
count += a * b * (b - 1) / 2 * c * (c - 1) * (c - 2) / 6
while 1:
    right += 1
    if right == len(players):
        break
    while players[right][0] / players[left][0] > 2:
        left += 1
    (a, b, c) = compute(players[left:right + 1])
    (x, y, z) = compute(players[left:right])
    count += a * b * (b - 1) / 2 * c * (c - 1) * (c - 2) / 6
    count -= x * y * (y - 1) / 2 * z * (z - 1) * (z - 2) / 6
print(int(count))
