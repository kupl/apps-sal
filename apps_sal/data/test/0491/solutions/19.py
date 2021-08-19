inner_data = input()
if int(inner_data) >= 0:
    print(inner_data)
else:
    inner_data = inner_data[1:]
    ee = ''
    if len(inner_data) >= 2:
        finded = 0
        for i in inner_data[::-1]:
            if i == inner_data[-2] and (not finded):
                finded = 1
                continue
            ee = ee + i
    if int(inner_data[-1]) > int(inner_data[-2]):
        if int(inner_data[-1]) == 0:
            if int(inner_data[-2]) != 0:
                print(0)
        elif int(inner_data[-1]) != 0:
            print('-' + inner_data[0:-1])
    elif int(inner_data[-1]) < int(inner_data[-2]):
        if int(ee[::-1]) == 0:
            print(0)
        else:
            print('-' + ee[::-1])
    elif int(inner_data[-1]) == int(inner_data[-2]):
        print('-' + ee[::-1])
    else:
        print(0)
