s = [int(i) % 3 for i in input()]

prev = 0
twice = 0
count = 0

for i in s:

    if i == 0:
        count += 1
        twice = 0
        prev = 0

    if i == 1:
        if prev == 2 or twice == 1:
            count += 1
            twice = 0
            prev = 0

        elif prev == 0:
            prev = 1
        else:
            twice = 1

    if i == 2:
        if prev == 1 or twice == 1:
            count += 1
            twice = 0
            prev = 0

        elif prev == 0:
            prev = 2
        else:
            twice = 1

print(count)
