t = int(input())

for _ in [0]*t:
    n, heads = list(map(int, input().split()))
    attacks = [list(map(int, input().split())) for _ in range(n)]
    max_damage = max(attacks)[0]
    turn_damage = max(x-y for x, y in attacks)

    if heads > max_damage and turn_damage <= 0:
        print(-1)
        continue
    if heads <= max_damage:
        print(1)
        continue

    x = heads-max_damage
    print((x+turn_damage-1) // turn_damage + 1)

