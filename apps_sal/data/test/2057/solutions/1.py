n = int(input())
a = list(map(int, input().split()))
now_time = 1
count_v = 1
last_time = [0 for i in range(2 * 10 ** 5 + 10)]
last_time[0] = 1
for i in range(n):
    if last_time[a[i]] > 0:
        last_time[a[i]] -= 1
    else:
        count_v += 1
    last_time[now_time] += 1
    now_time += 1
print(count_v)
