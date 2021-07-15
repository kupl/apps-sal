n, p = input().split()
n, p = int(n), int(p)

money = 0

apples = 0

pohyby = []
for _ in range(n):
    pohyby.append(input())

for pos, pohyb in enumerate(reversed(pohyby)):
    if pohyb == "half":
        apples *= 2
        money += apples / 2 * p
    elif pos == 0:
        apples = 1
        money += p / 2
    else:
        apples = apples * 2 + 1
        money += apples / 2 * p

print(int(money))
