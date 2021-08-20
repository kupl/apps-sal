for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    (l_1, r1) = list(map(int, input().split()))
    (l_2, r2) = list(map(int, input().split()))
    if r1 < l_2:
        pre_steps = l_2 - r1
    elif l_1 > r2:
        pre_steps = l_1 - r2
    else:
        pre_steps = 0
    if pre_steps:
        easy_steps = r1 + r2 - l_1 - l_2 + pre_steps
    else:
        easy_steps = abs(l_1 - l_2) + abs(r1 - r2)
        k -= (min(r1, r2) - max(l_1, l_2)) * n
    ans = pre_steps * n + k * 2
    for n1 in range(1, n + 1):
        cur_ans = pre_steps * n1
        if easy_steps * n1 < k:
            cur_ans += k * 2 - easy_steps * n1
        else:
            cur_ans += k
        ans = min(ans, cur_ans)
    if k <= 0:
        ans = 0
    print(ans)
