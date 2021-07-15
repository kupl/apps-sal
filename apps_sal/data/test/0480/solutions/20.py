def codeforces(max_point, start, finish, tram_speed, legs_speed,
               tram_point, direction):
    if tram_point == start:
        time_to_start = 0
    elif start > tram_point:
        if direction == 1:
            time_to_start = (start - tram_point) * tram_speed
        else:
            direction = -direction
            time_to_start = ((start - tram_point) * tram_speed +
                             tram_point * 2 * tram_speed)
    elif start < tram_point:
        if direction == -1:
            time_to_start = (tram_point - start) * tram_speed
        else:
            direction = -direction
            time_to_start = ((tram_point - start) * tram_speed +
                             (max_point - tram_point) * 2 * tram_speed)

    if start == finish:
        time_to_finish = 0
    elif finish > start:
        if direction == 1:
            time_to_finish = (finish - start) * tram_speed
        else:
            direction = -direction
            time_to_finish = ((finish - start) * tram_speed +
                              start * 2 * tram_speed)
    elif finish < start:
        if direction == -1:
            time_to_finish = (start - finish) * tram_speed
        else:
            direction = -direction
            time_to_finish = ((start - finish) * tram_speed +
                              (max_point - start) * 2 * tram_speed)

    tram_time = time_to_start + time_to_finish
    legs_time = abs(finish - start) * legs_speed
    return min(tram_time, legs_time)


max_point, start, finish = list(map(int, input().split()))
tram_speed, legs_speed = list(map(int, input().split()))
tram_point, direction = list(map(int, input().split()))

print((codeforces(max_point, start, finish, tram_speed, legs_speed,
                 tram_point, direction)))

