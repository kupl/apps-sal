def bitmake(digit):  # bit文字列生成（取り扱い注意）
    bit_list = list()

    for i in range(2 ** digit):
        bit = []
        for j in range(digit):  # このループが一番のポイント
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                bit.append(j)
        bit_list.append(bit)
    return bit_list


h, w, k = list(map(int, input().split()))
grid = [""] * h
for i in range(h):
    grid[i] = list(map(str, input()))
# print(grid)

bit_list = bitmake(h + w)
# print(bit_list)
blackh = [0] * h  # 横
blackw = [0] * w  # 縦
blacksum = 0
for i in range(h):
    for j in range(w):
        if(grid[i][j] == "#"):
            blackh[i] += 1
            blackw[j] += 1
            grid[i][j] = 1
            blacksum += 1
        else:
            grid[i][j] = 0
# print(blackh,blackw)
ans = 0
for i in range(2**(h + w)):
    bit = bit_list[i]  # h:0~(h-1),w:h~(h+w)-1
    remove = 0
    hight = []
    width = []
    for j in range(len(bit)):
        l = bit[j]
        if(l <= h - 1):
            remove += blackh[l]
            hight.append(l)
        else:
            ind = l - h
            remove += blackw[ind]
            width.append(ind)
    # print(hight,width)
    rid = 0
    for j in range(len(hight)):
        for l in range(len(width)):
            if(grid[hight[j]][width[l]] == 1):
                rid += 1

    if((blacksum - remove) + rid == k):
        # print(blacksum,remove,rid,"___",blacksum-remove+rid)
        ans += 1
print(ans)

# 2 3 2
# ..#
# ###
