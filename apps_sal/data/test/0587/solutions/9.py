def main():
    N, K = list(map(int, input().split()))
    sushi_list = list()
    for _ in range(N):
        t, d = list(map(int, input().split()))
        t -= 1
        sushi_list.append((t, d))
    sushi_list.sort(key=lambda s: s[1], reverse=True)
    neta_flag_list = [0] * N
    topk_extra_sushi_list = list()
    additional_sushi_list = list()
    point_topk = 0
    for k, sushi in enumerate(sushi_list):
        if k < K:
            if neta_flag_list[sushi[0]] == 1:
                topk_extra_sushi_list.append(sushi)
            point_topk += sushi[1]
        else:
            if neta_flag_list[sushi[0]] == 0:
                additional_sushi_list.append(sushi)
        neta_flag_list[sushi[0]] = 1
    n_neta = K - len(topk_extra_sushi_list)
    point_topk += n_neta ** 2
    d_extra, d_additional = 0, 0
    ans = point_topk
    n_additional_neta = min(K - n_neta, len(topk_extra_sushi_list), len(additional_sushi_list))
    for t in range(1, n_additional_neta + 1):
        n_cur_neta = n_neta + t
        d_extra += topk_extra_sushi_list[-t][1]
        d_additional += additional_sushi_list[t - 1][1]
        point = point_topk - d_extra + d_additional + (n_cur_neta**2 - n_neta**2)
        ans = max(ans, point)
    print(ans)


def __starting_point():
    main()


__starting_point()
