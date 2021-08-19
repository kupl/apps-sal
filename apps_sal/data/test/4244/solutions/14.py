n = int(input())
x = list(map(int, input().split()))
x_max = max(x)
x_min = min(x)
hp_min = 10000 * 100
for p in range(x_min, x_max + 1):
    hp = 0
    for x_i in x:
        hp += (x_i - p) ** 2
    if hp < hp_min:
        hp_min = hp
print(hp_min)
