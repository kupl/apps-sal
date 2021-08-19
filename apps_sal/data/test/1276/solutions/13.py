def abc162d_rgb_triplets():
    n = int(input())
    s = input()
    r_cnt = 0
    g_cnt = 0
    b_cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'R':
            r_cnt += 1
        elif s[i] == 'G':
            g_cnt += 1
        else:
            b_cnt += 1
    result = r_cnt * g_cnt * b_cnt
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            k = j + (j - i)
            if s[i] == s[j] or k >= n or s[i] == s[k] or (s[j] == s[k]):
                continue
            result -= 1
    print(result)


abc162d_rgb_triplets()
