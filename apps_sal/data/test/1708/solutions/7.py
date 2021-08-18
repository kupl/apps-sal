import sys
def read(): return list(map(int, sys.stdin.readline().split()))


write = sys.stdout.write

n, m = read()
dish = [0] + list(read())
dishes = sum(dish)
cost = [0] + list(read())

remain = []
for i in range(1, n + 1):
    remain.append(
        [cost[i], i]
    )
remain.sort(reverse=True)

for i in range(m):
    t, d = read()
    ans = 0

    if dishes == 0:
        write("0\n")

    elif dish[t] >= d:
        dishes -= d
        dish[t] -= d
        write(f"{cost[t]*d}\n")

    elif dish[t] < d:
        ans += dish[t] * cost[t]
        dishes -= dish[t]
        d -= dish[t]
        dish[t] = 0

        while d > 0 and dishes > 0:
            k = remain[-1][1]

            if dish[k] >= d:
                dish[k] -= d
                dishes -= d
                ans += cost[k] * d
                d = 0
            else:
                dishes -= dish[k]
                d -= dish[k]
                ans += cost[k] * dish[k]
                dish[k] = 0
                remain.pop()

        if d > 0 and dishes == 0:
            write("0\n")
        else:
            write(f"{ans}\n")
