from math import ceil
n, k = map(int, input().split())
d = list(map(int, input().split()))
s = list(map(int, input().split()))
fuel = 0
stor = 0
time = 0

for i in range(n):
    fuel += s[i]
    stor = max(stor, s[i])
    if fuel >= d[i]:
        fuel -= d[i]
        time += d[i]
    else:
        yy = ceil((d[i] - fuel) / stor)
        time += k * yy
        time += d[i]
        fuel += stor * yy
        fuel -= d[i]
print(time)
