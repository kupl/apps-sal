num, count_station, my_position = list(map(int, input().split()))
a = list(map(int, input().split()))
station_list = list(a)
space = num + 1
first_me_cost = 0
last_me_cost = 0

distance_me_first = my_position
distance_me_last = num - my_position

for i in station_list:
    if 1 <= i <= my_position - 1:
        first_me_cost += 1

for i in station_list:
    if my_position + 1 <= i < num:
        last_me_cost += 1

if first_me_cost > last_me_cost:
    print(last_me_cost)
elif last_me_cost > first_me_cost:
    print(first_me_cost)
elif last_me_cost == first_me_cost:
    print(first_me_cost)
