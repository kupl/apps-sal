n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
curr_streak = 0
curr_power = a[0]
for i in range(1, n):
    if curr_power > a[i]:
        curr_streak += 1
    else:
        curr_power = a[i]
        curr_streak = 1
    if curr_streak >= k:
        print(curr_power)
        return
print(curr_power)


