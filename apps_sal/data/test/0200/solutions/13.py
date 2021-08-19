def dprint(str):
    pstatus = False
    if pstatus == True:
        print(str)


def check_cat():
    from math import ceil
    from operator import add
    h_string = input()
    speed_string = input()
    (h_cat, h_app) = list(map(int, h_string.split()))
    (day_up, day_down) = list(map(int, speed_string.split()))
    day_sub = [4 * day_up, 8 * day_up, -12 * day_down]
    flag = False
    day_loc = [0, h_cat]
    current_pos = day_loc[1]
    day_counter = 0
    i1 = 0
    if sum(day_sub) <= 0:
        if h_cat + day_sub[1] >= h_app:
            return 0
        else:
            return -1
    while not flag:
        if current_pos >= h_app:
            flag = True
            break
        else:
            i1 += 1
            current_pos += day_sub[i1 % 3]
            day_loc.append(current_pos)
    dprint(day_loc)
    day_counter = i1
    dprint(day_counter)
    dprint(day_counter % 3)
    return int(day_counter / 3)


output = check_cat()
print(output)
