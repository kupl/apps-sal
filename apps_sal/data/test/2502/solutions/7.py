def z_alg(S):
    N = len(S)
    Z = [0] * N
    Z[0] = N
    i, j = 1, 0
    while i < N:
        while i + j < N and S[j] == S[i + j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < N and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        i += k
        j -= k
    return Z


def main():
    S = input()
    T = input()
    REP_S = ''
    target_len = len(S) + len(T) - 1
    while len(REP_S) < target_len:
        REP_S += S

    # Z-algorithmでREP_S中に含まれるTの場所を調べる
    T_REP_S = T + REP_S
    z = z_alg(T_REP_S)
    location_list = list()
    for i in range(len(S)):
        if z[i + len(T)] >= len(T):
            location_list.append(i)

    # Tがなければ0を出力して終了
    if len(location_list) == 0:
        print(0)
        return

    # グラフを作り、最長パスに含まれるノード数が答え（ループがあったら-1）
    node_flag_list = [0] * len(S)
    for n in location_list:
        node_flag_list[n] = 1
    depth_list = [-1] * len(S)
    for n in location_list:
        if depth_list[n] >= 0:
            continue
        cur_node = n
        d, has_loop = 0, False
        while node_flag_list[cur_node] == 1:
            depth_list[cur_node] = d
            d += 1
            cur_node = (cur_node + len(T)) % len(S)
            if cur_node == n:
                has_loop = True
                break
        if has_loop:
            print(-1)
            return

    print(max(depth_list) + 1)


def __starting_point():
    main()
__starting_point()
