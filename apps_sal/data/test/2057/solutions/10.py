n = int(input())
a = list(map(int, input().split()))
time = [-1] * (n + 1)
time[0] = 1
count = 1
for i in range(n):
    cur_time = i + 1
    if time[a[i]] != -1:
        time[a[i]], time[cur_time] = -1, time[a[i]]
    else:
        count += 1
        time[cur_time] = count
print(count)
