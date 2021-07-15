from sys import stdin

n = int(stdin.readline())

a = [int(x) for x in stdin.readline().split()]

pizza_free_today = False

result = 'NO'

for teams in a:
    if pizza_free_today:
        teams -= 1
        pizza_free_today = False
    if teams < 0:
        break
    if teams % 2 == 0:
        pass
    else:
        pizza_free_today = True
else:
    if not pizza_free_today:
        result = 'YES'

print(result)

