(n, k) = map(int, input().split())
raw_list = list()
for i in range(0, n):
    raw_list.append(input())
place_list = list()
count_list = list()
for (raw_index, raw) in enumerate(raw_list):
    for (place_index, place) in enumerate(raw):
        if place == '.':
            count = 0
            if place_index > 0 and raw[place_index - 1] == 'S':
                count += 1
            if place_index < len(raw) - 1 and raw[place_index + 1] == 'S':
                count += 1
            place_list.append((raw_index, place_index))
            count_list.append(count)
min_list = list()
put_list = list()
for i in range(0, k):
    min_list.append(count_list.index(min(count_list)))
    put_list.append(place_list[min_list[i]])
    del count_list[min_list[i]]
    del place_list[min_list[i]]
new_raw_list = list()
here = False
for (raw_index, raw) in enumerate(raw_list):
    new_raw = str()
    for (place_index, place) in enumerate(raw):
        for i in range(0, len(min_list)):
            if raw_index == put_list[i][0] and place_index == put_list[i][1]:
                new_raw += 'x'
                here = True
                break
            else:
                continue
        if here == False:
            new_raw += place
        else:
            here = False
    new_raw_list.append(new_raw)
result = 0
alive = ['S', 'P', 'x']
for raw in new_raw_list:
    for (place_index, place) in enumerate(raw):
        if place == 'S':
            if place_index != 0:
                if raw[place_index - 1] in alive:
                    result += 1
            if place_index != len(raw) - 1:
                if raw[place_index + 1] in alive:
                    result += 1
print(result)
for i in range(0, n):
    print(new_raw_list[i])
