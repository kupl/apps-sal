doctors_nr = int(input())
doctor_idx___start_day_idx = []
doctor_idx___delta = []
for _ in range(doctors_nr):
    (start_day_idx, delta) = (int(x) for x in input().split())
    doctor_idx___start_day_idx.append(start_day_idx)
    doctor_idx___delta.append(delta)
doctors_visited_nr = 0
for day_idx in range(1, 3000000):
    curr_start_day_idx = doctor_idx___start_day_idx[doctors_visited_nr]
    curr_delta = doctor_idx___delta[doctors_visited_nr]
    if day_idx >= curr_start_day_idx and day_idx % curr_delta == curr_start_day_idx % curr_delta:
        doctors_visited_nr += 1
        if doctors_visited_nr == doctors_nr:
            print(day_idx)
            quit()
