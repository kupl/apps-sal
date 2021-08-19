def bitmake(digit):
    bit_list = list()
    for i in range(2 ** digit):
        bit = []
        for j in range(digit):
            if i >> j & 1:
                bit.append(j)
        bit_list.append(bit)
    return bit_list


(h, w, k) = list(map(int, input().split()))
grid = [''] * h
for i in range(h):
    grid[i] = list(map(str, input()))
bit_list = bitmake(h + w)
blackh = [0] * h
blackw = [0] * w
blacksum = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            blackh[i] += 1
            blackw[j] += 1
            grid[i][j] = 1
            blacksum += 1
        else:
            grid[i][j] = 0
ans = 0
for i in range(2 ** (h + w)):
    bit = bit_list[i]
    remove = 0
    hight = []
    width = []
    for j in range(len(bit)):
        l = bit[j]
        if l <= h - 1:
            remove += blackh[l]
            hight.append(l)
        else:
            ind = l - h
            remove += blackw[ind]
            width.append(ind)
    rid = 0
    for j in range(len(hight)):
        for l in range(len(width)):
            if grid[hight[j]][width[l]] == 1:
                rid += 1
    if blacksum - remove + rid == k:
        ans += 1
print(ans)
