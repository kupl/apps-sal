forecast_list = list(input())
happened_list = list(input())
hit_count = 0
for (f, h) in zip(forecast_list, happened_list):
    if f == h:
        hit_count += 1
print(hit_count)
