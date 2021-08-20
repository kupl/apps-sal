(n, c) = map(int, input().split())
clock = []
counter_clock = []
for i in range(n):
    (x, v) = map(int, input().split())
    clock.append([x, v])
    counter_clock.append([c - x, v])
clock.sort()
counter_clock.sort()
clock_ac = [0]
counter_clock_ac = [0]
for i in range(n):
    v = clock[i][1]
    clock_ac.append(clock_ac[-1] + v)
    v2 = counter_clock[i][1]
    counter_clock_ac.append(counter_clock_ac[-1] + v2)
for i in range(n):
    x = clock[i][0]
    clock_ac[i + 1] -= x
    x2 = counter_clock[i][0]
    counter_clock_ac[i + 1] -= x2
max_clock_ac = [0]
max_counter_clock_ac = [0]
for i in range(n):
    max_clock_ac.append(max(max_clock_ac[-1], clock_ac[i + 1]))
    max_counter_clock_ac.append(max(max_counter_clock_ac[-1], counter_clock_ac[i + 1]))
ans = max(max_clock_ac[n], max_counter_clock_ac[n])
for i in range(n):
    ans = max(ans, clock_ac[i + 1] - clock[i][0] + max_counter_clock_ac[n - i - 1])
    ans = max(ans, counter_clock_ac[i + 1] - counter_clock[i][0] + max_clock_ac[n - i - 1])
print(ans)
