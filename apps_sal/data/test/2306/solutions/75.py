n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
tmp = 0
e_t = []
for i in t:
    tmp += i
    e_t.append(tmp)


def calc_end_speed(s):
    end_time = e_t[s]
    ma = 10 ** 10
    for i in range(s + 1, n):
        ma = min(e_t[i - 1] - end_time + v[i], ma)
    return min(e_t[-1] - end_time, v[s], ma)


ans = 0
start_speed = 0
for sect in range(n):
    end_speed = min(calc_end_speed(sect), start_speed + t[sect])
    turn_time = (t[sect] + end_speed - start_speed) / 2
    acce_end = min(v[sect] - start_speed, turn_time)
    dece_start = max(t[sect] - (v[sect] - end_speed), turn_time)
    max_speed = start_speed + acce_end
    ans += (start_speed + max_speed) * acce_end / 2
    ans += max_speed * (dece_start - acce_end)
    ans += (end_speed + max_speed) * (t[sect] - dece_start) / 2
    start_speed = end_speed
print(ans)
