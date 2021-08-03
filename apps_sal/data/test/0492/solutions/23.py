pos1, pos2 = input().split()
turns_nr = int(input())

if turns_nr % 2 == 0:
    print('undefined')
    return
elif turns_nr % 4 == 1:
    lst = '<^>v<^>v'
    for idx1, sym1 in enumerate(lst):
        if sym1 == pos1:
            if lst[idx1 - 1] == pos2:
                print('ccw')
                return
            elif lst[idx1 + 1] == pos2:
                print('cw')
                return
elif turns_nr % 4 == 3:
    lst = '<^>v<^>v'
    for idx1, sym1 in enumerate(lst):
        if sym1 == pos1:
            if lst[idx1 - 1] == pos2:
                print('cw')
                return
            elif lst[idx1 + 1] == pos2:
                print('ccw')
                return
