n = int(input())
a = list(map(int, input().split()))
pm_sum = 0
pm_count = 0
mp_sum = 0
mp_count = 0
for i in range(n):
    pm_sum += a[i]
    mp_sum += a[i]
    if i % 2 == 0:
        pm_d = max(0, 1 - pm_sum)
        mp_d = max(0, mp_sum - (-1))
        pm_sum += pm_d
        mp_sum -= mp_d
    else:
        pm_d = max(0, pm_sum - (-1))
        mp_d = max(0, 1 - mp_sum)
        pm_sum -= pm_d
        mp_sum += mp_d
    pm_count += pm_d
    mp_count += mp_d
print(min(pm_count, mp_count))
