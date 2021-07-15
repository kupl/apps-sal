n = int(input())
notes = [int(x) for x in input().split()]
greatest_cave = 1
visits = {0: 1}
for time, curr in enumerate(notes, start=1):
    if curr in visits and visits[curr] != -1:
        visits[time] = visits[curr]
        visits[curr] = -1
    else:
        greatest_cave += 1
        visits[time] = greatest_cave
print(greatest_cave)

