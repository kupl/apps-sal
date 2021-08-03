N, M = map(int, input().split())
road_list = []
for i in range(M):
    road_list.append(list(map(int, input().split())))

road_dict = {}
for road in road_list:
    first_city = road[0]
    second_city = road[1]
    first_city_road_list = road_dict.get(first_city, [])
    first_city_road_list.append(second_city)
    road_dict[first_city] = first_city_road_list

    second_city_road_list = road_dict.get(second_city, [])
    second_city_road_list.append(first_city)
    road_dict[second_city] = second_city_road_list

for i in range(1, N + 1):
    city_road_list = road_dict.get(i, [])
    road_num = len(city_road_list) if city_road_list != [] else 0
    print(road_num)
