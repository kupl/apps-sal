fly_times = [int(v) for v in input().split(' ')]
min_t = 10 ** 9
for i in range(3):
    result = 0
    for j in range(3):
        if i == j:
            continue
        result += fly_times[j]
    if result < min_t:
        min_t = result
print(min_t)
