n = int(input())
folders = []
loss_count = 0
day_count = 0
for x in map(int, input().split()):
    if x < 0:
        if loss_count == 2:
            folders.append(day_count)
            loss_count = 1
            day_count = 0
        else:
            loss_count += 1
    day_count += 1
folders.append(day_count)
print(len(folders))
print(' '.join(map(str, folders)))

