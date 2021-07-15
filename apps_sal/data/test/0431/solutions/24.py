from collections import Counter
import sys

def left_time(floor):
    light_counter = Counter(floor)
    # print(light_counter)
    # print(light_counter['1'])
    if light_counter['1'] == 0:
        return 0
    else:
        last_light_search = 1
        while last_light_search <= len(floor):
            # print(last_light_search)
            if floor[-last_light_search] == '1':
                return((len(floor) - last_light_search) * 2)
                break
            else:
                last_light_search += 1
        

def right_time(floor):
    light_counter = Counter(floor)
    if light_counter['1'] == 0:
        return 0
    else:
        last_light_search = 0
        while True:
            if floor[last_light_search] == '1':
                return ((len(floor) - last_light_search - 1) * 2)
                break
            else:
                last_light_search += 1

floors_nr, rooms_nr = (int(x) for x in input().split())
building_scheme = []
worth_counting_flag = False
for i in range(floors_nr):
    floor_i = input()
    c = Counter(floor_i)
    if not worth_counting_flag and c['1'] > 0:
        worth_counting_flag = True
    if worth_counting_flag:
        building_scheme.append(floor_i)

if len(building_scheme) == 0:
    print(0)
    return
    
optimal_time = [(-1, 10000)]

last_floor = building_scheme[0]
building_scheme = building_scheme[1:]
for floor in building_scheme[::-1]:
    prefix_left, prefix_right = optimal_time[-1]
    
    keep_right_left = rooms_nr + 1 + prefix_left + 1
    keep_right_right = right_time(floor) + prefix_right + 1
    keep_right = min(keep_right_left, keep_right_right)
    
    keep_left_left = left_time(floor) + prefix_left + 1
    keep_left_right = rooms_nr + 1 + prefix_right + 1
    keep_left = min(keep_left_left, keep_left_right)
    
    optimal_time.append((keep_left, keep_right))

# print(optimal_time)

last_floor_time = min(optimal_time[-1][0] + 1 + left_time(last_floor) // 2, optimal_time[-1][1] + 1 + right_time(last_floor) // 2)
print(last_floor_time)
    
    



