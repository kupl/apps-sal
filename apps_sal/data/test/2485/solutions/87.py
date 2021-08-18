def main():
    H, W, M = list(map(int, input().split()))
    hw = [tuple(list(map(int, input().split()))) for _ in [0] * M]
    hw_set = set(hw)
    h_count = [0 for i in range(H + 1)]
    w_count = [0 for i in range(W + 1)]
    for h, w in hw:
        h_count[h] += 1
        w_count[w] += 1
    h_m = max(h_count)
    w_m = max(w_count)
    h_list = []
    w_list = []
    for i in range(H + 1):
        if h_count[i] == h_m:
            h_list.append(i)
    for i in range(W + 1):
        if w_count[i] == w_m:
            w_list.append(i)
    for i in h_list:
        for j in w_list:
            if (i, j) not in hw_set:
                print((h_m + w_m))
                return
    print((h_m + w_m - 1))


main()
