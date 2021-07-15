n, k = list(map(int,input().split()))

days = input().split()

changes = 0

for day in range(n-1):
    day1 = int(days[day])
    day2 = int(days[day+1])
    day2p = k-(day1+day2)
    if day2p > 0:
        changes+= day2p
        days[day+1] = str(day2+day2p)

print(changes)

print(" ".join(days))

