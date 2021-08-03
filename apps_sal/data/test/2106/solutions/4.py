estradas, k = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]


fuel = 0
time = 0

currMax = 0

for i in range(estradas):
    fuel += s[i]
    currMax = max(currMax, s[i])

    while(fuel < d[i]):
        time += k
        fuel += currMax

    fuel -= d[i]
    time += d[i]
print(time)
