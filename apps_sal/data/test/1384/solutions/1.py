length = int(input())
array = list(map(int, input().split()))

count = []
total = 0

for k in range(length):
    if array[length - 1 - k] == 1:
        total += 1
    count.append(total)
count.reverse()

total = 0
maximum = 0
for k in range(length):
    if array[k] == 0:
        total += 1

    maximum = max(maximum, total + count[k])

print(maximum)

