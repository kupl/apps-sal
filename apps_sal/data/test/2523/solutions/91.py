def rle(s):
    # ex. '01100011110' -> [1 2 3 4 1]
    before_c = s[0]
    ret = list()
    cnt = 0
    for c in s:
        if before_c == c:
            cnt += 1
        else:
            ret.append(cnt)
            before_c = c
            cnt = 1
    if cnt > 0:
        ret.append(cnt)
    return ret


def main():
    S = input()
    N = len(S)
    seq_cnt = rle(S)
    if len(seq_cnt) == 1:
        print(seq_cnt[0])
        return
    if len(seq_cnt) == 2:
        print(max(seq_cnt))
        return
    # cumsum
    cumsum_seq_cnt = [0 for _ in range(len(seq_cnt))]
    rev_cumsum_seq_cnt = [0 for _ in range(len(seq_cnt))]
    cumsum_seq_cnt[0] = seq_cnt[0]
    rev_cumsum_seq_cnt[0] = seq_cnt[-1]
    for i in range(1, len(seq_cnt)):
        cumsum_seq_cnt[i] = cumsum_seq_cnt[i - 1] + seq_cnt[i]
        rev_cumsum_seq_cnt[i] = rev_cumsum_seq_cnt[i - 1] + seq_cnt[-1 - i]
    # search
    max_k = cumsum_seq_cnt[0]
    rev_max_k = rev_cumsum_seq_cnt[0]
    for i in range(1, len(seq_cnt)):
        k = cumsum_seq_cnt[i]
        if k <= N - cumsum_seq_cnt[i - 1]:
            max_k = k
        rev_k = rev_cumsum_seq_cnt[i]
        if rev_k <= N - rev_cumsum_seq_cnt[i - 1]:
            rev_max_k = rev_k
    print(max([max_k, rev_max_k]))


def __starting_point():
    main()


__starting_point()
