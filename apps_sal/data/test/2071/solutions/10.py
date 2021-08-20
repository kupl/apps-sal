def main():
    [n] = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    sums = []
    for i in range(n):
        if len(sums) == 0:
            sums.append(a[-1] + b[-1])
        else:
            sums.append(sums[-1] + a[-i - 1] + b[-i - 1])
    bottom_to_top = []
    top_to_bottom = []
    for i in range(n):
        if i == 0:
            bottom_to_top.append(a[-1])
            top_to_bottom.append(b[-1])
        else:
            bottom_to_top.append(bottom_to_top[-1] + sums[i - 1] + a[-i - 1] * (2 * i + 1))
            top_to_bottom.append(top_to_bottom[-1] + sums[i - 1] + b[-i - 1] * (2 * i + 1))
    best_t = []
    best_b = []
    for i in range(n):
        if i == 0:
            best_t.append(top_to_bottom[0])
            best_b.append(bottom_to_top[0])
        else:
            x = b[-i - 1] + 2 * sums[i - 1] + best_b[i - 1]
            y = a[-i - 1] + 2 * sums[i - 1] + best_t[i - 1]
            best_t.append(max([x, top_to_bottom[i]]))
            best_b.append(max([y, bottom_to_top[i]]))
    print(best_t[-1])


main()
