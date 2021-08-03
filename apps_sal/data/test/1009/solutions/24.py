def __starting_point():
    n, k = list(map(int, input().split()))
    s_list = list(map(int, input().split()))

    a_list = s_list[:n - min(n, 2 * k - n)]
    b_list = reversed(a_list)
    c_list = [a + b for a, b in zip(a_list, b_list)]
    print(max(max(c_list or [0]), max(s_list)))


__starting_point()
