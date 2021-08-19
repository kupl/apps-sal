_ = input()
numbers = {}
for (index, num) in enumerate(input().split()):
    num = int(num)
    try:
        numbers[num].append(index)
    except:
        numbers[num] = [index]
temp = {}
size = 0
for (num, ind) in numbers.items():
    try:
        prog = ind[1] - ind[0]
    except IndexError:
        temp[num] = 0
        size += 1
        continue
    for i in range(2, len(ind)):
        new_prog = ind[i] - ind[i - 1]
        if new_prog != prog:
            prog = -1
            break
    if prog != -1:
        temp[num] = prog
        size += 1
print(size)
keys = sorted(temp.keys())
for key in keys:
    print(key, temp[key])
