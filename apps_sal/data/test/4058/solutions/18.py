n, r = list(map(int, input().split()))
a = list(map(int, input().split()))
res = 0
last_heater_pos = -r
while (n - last_heater_pos > r) or (last_heater_pos < 0):
    next_heaters_pos = [i for i in range(max(0, last_heater_pos + 1), min(last_heater_pos + 2 * r, n)) if a[i] == 1]
    if next_heaters_pos:
        last_heater_pos = max(next_heaters_pos)
        res += 1
        # print('found', last_heater_pos, 'among', next_heaters_pos)
    else:
        print(-1)
        return

print(res)
