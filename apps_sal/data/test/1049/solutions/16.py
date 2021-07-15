n,d = list(map(int, input().split()))

consecutiveDays = 0

currentMax = 0
for item in range(d):
    current = input()
    if '0' in current:
        currentMax += 1
        consecutiveDays = max(consecutiveDays, currentMax)
    else:
        currentMax = 0

print(consecutiveDays)

