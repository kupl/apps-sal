lines = [[int(num) for num in input().split()] for _ in range(2)]
n = lines[0][0]
skewers = sorted(lines[1])
total = 0
for i in range(n):
    total += skewers[2 * i]
print(total)
