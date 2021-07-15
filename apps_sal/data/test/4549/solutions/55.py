h, w = [int(x) for x in input().split()]
s_list = [input() for _ in range(h)]

iso_flag = [[True] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s_list[i][j] == ".":
            continue

        flag_r = True
        if j < w - 1 and s_list[i][j + 1] == "#":
            flag_r = iso_flag[i][j + 1] = False
        
        flag_d = True
        if i < h - 1 and s_list[i + 1][j] == "#":
            flag_d = iso_flag[i + 1][j] = False
        
        if iso_flag[i][j] and flag_r and flag_d:
            print("No")
            return
print("Yes")
