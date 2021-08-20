def main():
    (n, w) = list(map(int, input().split()))
    (w1, v1) = list(map(int, input().split()))
    values = [[] for _ in range(4)]
    values[0].append(v1)
    for _ in range(n - 1):
        (wi, vi) = list(map(int, input().split()))
        values[wi - w1].append(vi)
    for i in range(4):
        values[i].sort(reverse=True)
    prefix = [[0] for _ in range(4)]
    for i in range(4):
        for j in range(len(values[i])):
            prefix[i].append(prefix[i][-1] + values[i][j])
    max_ans = 0
    tot_val = [0] * 4
    tot_weights = [0] * 4
    for i in range(min(len(values[0]), w // w1) + 1):
        tot_val[0] = prefix[0][i]
        tot_weights[0] = w1 * i
        for j in range(min(len(values[1]), w // (w1 + 1)) + 1):
            tot_val[1] = tot_val[0] + prefix[1][j]
            tot_weights[1] = tot_weights[0] + (w1 + 1) * j
            if tot_weights[1] > w:
                break
            for k in range(min(len(values[2]), w // (w1 + 2)) + 1):
                tot_val[2] = tot_val[1] + prefix[2][k]
                tot_weights[2] = tot_weights[1] + k * (w1 + 2)
                if tot_weights[2] > w:
                    break
                diff = w - tot_weights[2]
                min_select = min(diff // (w1 + 3), len(values[3]))
                tot_val[3] = tot_val[2] + prefix[3][min_select]
                tot_weights[3] = tot_weights[2] + min_select * (w1 + 3)
                max_ans = max(max_ans, tot_val[3])
    print(max_ans)


def __starting_point():
    main()


__starting_point()
