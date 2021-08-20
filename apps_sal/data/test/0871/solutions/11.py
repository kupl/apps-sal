(num_landings, min_interval) = (int(x) for x in input().split())
landings = [[int(x) for x in input().split()] for _ in range(num_landings)]
landings_in_minutes = [-min_interval - 1] + [60 * clock[0] + clock[1] for clock in landings] + [float('inf')]
for (left_landing, right_landing) in zip(landings_in_minutes[:-1], landings_in_minutes[1:]):
    if left_landing + 2 * min_interval + 2 <= right_landing:
        takeoff = left_landing + 1 + min_interval
        break
takeoff_hours = takeoff // 60
takeoff_mins = takeoff % 60
print(takeoff_hours, takeoff_mins)
