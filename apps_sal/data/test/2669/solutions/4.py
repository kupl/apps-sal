# cook your dish here
size = int(input())
starting_times = list(map(int, input().split()))
ending_times = list(map(int, input().split()))

tasks_indices_set = set()

last_timing = 0

for i in range(size):
    # print("Index:", i, "& last_timing:", last_timing)
    # if i==0: tasks_indices_set.add(i)
    if starting_times[i] >= last_timing:
        tasks_indices_set.add(i)
        last_timing = ending_times[i]
        for j in range(i + 1, size):
            if ending_times[i] <= starting_times[j]:
                tasks_indices_set.add(j)
                last_timing = ending_times[j]
                break

print(*sorted(tasks_indices_set))
