num_of_switch, light = list(map(int, input().split()))
ligth_list = [list(map(int, input().split())) for _ in range(light)]
on_list = list(map(int, input().split()))

num_of_patern = 2 ** num_of_switch
patern = 0

for i in range(num_of_patern):
    on = []
    light_counter = 0
    for j in range(num_of_switch):  # スイッチのオンの場所
        if ((i >> j) & 1):
            on.append(j + 1)
    for j in range(light):  # どの電球が付いているかの判定
        count = 0
        num_connect = ligth_list[j][0]
        # print(on)
        if on_list[j] == 1:
            for n in range(len(on)):
                if on[n] in ligth_list[j][1:]:
                    count += 1
            if count % 2 == 1:
                light_counter += 1
        else:
            for m in range(len(on)):
                if on[m] in ligth_list[j][1:]:
                    count += 1
            if count % 2 == 0:
                light_counter += 1
    if light_counter == light:
        # print(i)
        patern += 1
    del on[:]
print(patern)
