dishes = []
for i in range(5):
    dishes.append(int(input()))

wasted_times = []
for dish in dishes:
    wasted_time = (10 - (dish % 10)) % 10
    wasted_times.append(wasted_time)

wasted_times.sort()
del wasted_times[-1]

ans = sum(dishes) + sum(wasted_times)
print(ans)
