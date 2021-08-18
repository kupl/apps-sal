from collections import deque
rooms_number, cows_number = list(map(int, input().split()))
rooms = input()
free_rooms = [i for i in range(rooms_number) if rooms[i] == '0']


def binary_search(left, right, item):
    nonlocal free_rooms
    while right - left > 1:
        center = left + (right - left) // 2
        if free_rooms[center] > item:
            right = center
        else:
            left = center
    return left


min_distation_to_farthest_cow = 10**20
best_min_distation_to_farthest_cow = cows_number // 2 + cows_number % 2
for i in range(len(free_rooms) - cows_number):
    left = free_rooms[i]
    right = free_rooms[i + cows_number]
    center = left + (right - left) // 2
    j = binary_search(i, i + cows_number, center)
    if free_rooms[j] == center:
        distation_to_farthest_cow = right - center
    else:
        distation_to_farthest_cow = min(right - free_rooms[j], free_rooms[j + 1] - left)
    if min_distation_to_farthest_cow > distation_to_farthest_cow:
        min_distation_to_farthest_cow = distation_to_farthest_cow
    if distation_to_farthest_cow == best_min_distation_to_farthest_cow:
        break
print(min_distation_to_farthest_cow)
