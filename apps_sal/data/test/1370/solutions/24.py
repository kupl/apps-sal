(h, w, k) = list(map(int, input().split()))
choco = [list(map(int, list(input()))) for i in range(h)]
choco_cumsum = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    choco_cumsum[i][0] = choco[i][0]
    for j in range(1, w):
        choco_cumsum[i][j] = choco_cumsum[i][j - 1] + choco[i][j]
ans = h + w + 1
for h_cut in range(2 ** (h - 1)):
    num_cut_init = bin(h_cut).count('1')
    num_cut = num_cut_init
    w_last_cut_pos = -1
    valid = True
    count_white = [0] * (num_cut_init + 1)
    temp_dict = {}
    idx = 0
    temp_dict[0] = idx
    for i in range(1, h):
        if h_cut & 2 ** (-i + h - 1):
            idx += 1
        temp_dict[i] = idx
    iw = 0
    while iw < w:
        for ih in range(h):
            count_white[temp_dict[ih]] += choco[ih][iw]
        condition = max(count_white) > k
        if condition:
            if w_last_cut_pos < iw - 1:
                num_cut += 1
                w_last_cut_pos = iw - 1
                count_white = [0] * (num_cut_init + 1)
            else:
                valid = False
                break
        else:
            iw += 1
    if valid:
        ans = min(ans, num_cut)
print(ans)
