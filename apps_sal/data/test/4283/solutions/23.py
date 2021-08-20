n = int(input().strip())
numbers = list(map(int, input().strip().split(' ')))
numbers.sort()
start = 0
current = 0
l = []
tot = 0
while current < len(numbers) and start < len(numbers):
    if numbers[current] - numbers[start] > 5:
        start = start + 1
        l.append(tot)
        tot -= 1
    else:
        tot += 1
        current += 1
if len(l) > 0:
    print(max(tot, max(l)))
else:
    print(tot)
