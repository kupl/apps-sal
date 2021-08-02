n = int(input())

time_count_pairs = {}

for i in range(n):
    time = input()
    if not time_count_pairs.get(time):
        time_count_pairs[time] = 1
    else:
        time_count_pairs[time] += 1

count_max = 0

for i in list(time_count_pairs.values()):
    if i > count_max:
        count_max = i

print(count_max)
