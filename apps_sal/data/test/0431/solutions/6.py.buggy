import itertools

n, m = list(map(int, input().split()))

floors = []
max_lit = -1
for floor_n in range(n - 1, -1, -1):
    cur_floor = input()
    floors.insert(0, cur_floor)
    if max_lit == -1 and any(c == '1' for c in cur_floor):
        max_lit = floor_n + 1

if max_lit == -1:
    print('0')
    return


def calc_path(path):
    left = True
    result = 0
    for floor in range(max_lit):
        switch_stairs = path[floor]
        if left:
            pos = floors[floor].rfind('1')
            dist = 0 if pos == -1 else pos
        else:
            pos = floors[floor].find('1')
            dist = 0 if pos == -1 else m + 1 - pos
        is_last = floor == max_lit - 1
        result += dist
        if switch_stairs:
            if not is_last:
                result += m + 1 - dist
            left = not left
        else:
            if not is_last:
                result += dist
        if not is_last:
            result += 1
    return result


min_v = -1

for p in itertools.product([False, True], repeat=max_lit):
    v = calc_path(p)
    if min_v == -1 or min_v > v:
        min_v = v

print(min_v)
