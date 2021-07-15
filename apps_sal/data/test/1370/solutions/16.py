h, w, k = list(map(int, input().split()))

choco = [list(map(int, list(input()))) for i in range(h)]

ans = h + w + 1

for h_cut in range(2**(h-1)):
    # 上位ビットが上側。1が切る、0が切らない
    num_cut_yoko = bin(h_cut).count("1") # 立っているビットの個数
    num_cut = num_cut_yoko
    w_last_cut_pos = -1
    valid = True

    count_white = [0] * (num_cut_yoko + 1)
    temp_dict = {}
    idx = 0
    temp_dict[0] = idx
    for i in range(1, h):
        # print('idx', 2 ** (-i+h-1) )
        if h_cut & (2 ** (-i+h-1)):
            idx += 1
        # idx += h_cut & (2 ** (h-1) - i)
        temp_dict[i] = idx
    # print(temp_dict)

    iw = 0
    while iw < w:

        for ih in range(h):
            count_white[temp_dict[ih]] += choco[ih][iw]
        # print(iw, count_white)

        condition = max(count_white) > k
        if condition:
            if w_last_cut_pos < iw-1:
                # もしそこで切ってkを超えるなら、その手前で切る
                num_cut += 1
                w_last_cut_pos = iw - 1
                count_white = [0] * (num_cut_yoko + 1)
                # print('iw: ', iw, 'last: ', w_last_cut_pos)

            else:
                # 1つしか動かしてないのに、Kマスを超えてしまった場合は、この横の切り方では達成不可能なので次のh_cutに
                valid = False
                break
        
        else:
            iw += 1
    
    if valid:
        ans = min(ans, num_cut)
    # print(num_cut)

print(ans)

