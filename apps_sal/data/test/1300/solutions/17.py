line = input().split()
n = int(line[0])
c = int(line[1])
line = [int(x) for x in input().split()]

base_ans = 0
for num in line:
    if num == c:
        base_ans += 1

lut = {}
best_delta = 0
for num in line:
    if num == c:
        to_delete = []
        for key in lut:
            lut[key] -= 1
            if lut[key] <= 0:
                to_delete.append(key)
        for key in to_delete:
            del lut[key]
    else:
        if num in lut:
            lut[num] += 1
        else:
            lut[num] = 1
        
        if lut[num] >= best_delta:
            best_delta = lut[num]

print(base_ans + best_delta)

