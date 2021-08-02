n = int(input())
times = list(map(int, input().split()))
m = int(input())
drinks = []
for _ in range(m):
    drink = list(map(int, input().split()))
    drinks.append(drink)

for drink in drinks:
    time = 0
    copy = times.copy()
    copy[drink[0] - 1] = drink[1]
    for i in copy:
        time += i
    print(time)
