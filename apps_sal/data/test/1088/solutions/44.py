def main():
    law = 998244353
    n, k = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for i in range(n)]
    t_mat = [[mat[j][i] for j in range(n)] for i in range(n)]
    print(((line_pattern_counter_mod(mat, n, k, law) * line_pattern_counter_mod(t_mat, n, k, law)) % law))
    return


def line_pattern_counter_mod(mat, n, k, law):
    min_swapable = [i for i in range(n)]
    swappable_count = [0 for _ in range(n)]
    ret = 1
    for x in range(n):
        swappable_array = [x]
        min_ind = min_swapable[x]
        for y in range(n):
            if swappable(mat[x], mat[y], n, k):
                swappable_array.append(y)
                min_ind = min(min_ind, min_swapable[y])
        for ind in swappable_array:
            min_swapable[ind] = min_ind
    for m in range(n):
        swappable_count[min_swapable[m]] += 1
    for count in swappable_count:
        ret = (ret * fact_mod(count, law)) % law
    return ret


def swappable(l_1, l_2, n, k):
    for j in range(n):
        if l_1[j] + l_2[j] > k:
            return False
    return True


def fact_mod(m, law, acc=1):
    if m == 0:
        return acc
    return fact_mod(m - 1, law, (acc * m) % law)


def __starting_point():
    main()


__starting_point()
