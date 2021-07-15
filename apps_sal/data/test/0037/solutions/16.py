black, white, health = map(int, input().split())
damage = [False] * (health + 1 + max(white, black))
damage[0] = True
for i in range(health):
    if damage[i]:
        damage[i + black] = True
        damage[i + white] = True

if damage[health]:
    print('Yes')
else:
    print('No')
