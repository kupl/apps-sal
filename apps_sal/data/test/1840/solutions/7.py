(s, b) = list(map(int, input().split(' ')))
ships = list(map(int, input().split(' ')))
bases = [tuple(map(int, input().split(' '))) for _ in range(b)]
bases.sort()
gold = [0] * (b + 1)
for i in range(b):
    gold[i + 1] = gold[i] + bases[i][1]


def find(x, inf, sup):
    while inf < sup:
        mid = (inf + sup) // 2
        if bases[mid][0] <= x:
            inf = mid + 1
        else:
            sup = mid
    return sup - 1


attacks = [0] * s
for (i, ship) in enumerate(ships):
    attacks[i] = gold[find(ship, 0, b) + 1]
print(' '.join(map(str, attacks)))
