_ = int(input())
total_time = sum(map(int, input().rstrip().split()))
m = int(input())
for i in range(0, m):
    [start_time, end_time] = list(map(int, input().rstrip().split()))
    if start_time >= total_time:
        print(start_time)
        return
    elif total_time <= end_time:
        print(total_time)
        return
print(-1)
