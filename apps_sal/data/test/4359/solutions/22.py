time = [int(input()) for _ in range(5)]
new_time = []
amari = 10
for x in time:
    if x % 10 == 0:
        new_time.append(x)
    else:
        amari = min(amari, x % 10)
        new_time.append(10 * (x // 10 + 1))
total = sum(new_time)
dead = 10 - amari
print(total - dead)
