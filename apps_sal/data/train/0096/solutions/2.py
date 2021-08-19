m = int(input())
for ii in range(m):
    n, T, a, b = list(map(int, input().split()))
    score = [a, b]
    d = list(map(int, input().split()))
    t = list(map(int, input().split()))
    easy = 0
    for d1 in d:
        if d1 == 0:
            easy += 1
    diff = list(zip(t, d))
    diff = sorted(diff)  # from least to greatest
    cnt = 0
    cur = 0
    ans = 0
    for i in range(n):
        t, d = diff[i]
        # print('----',i, cur, cnt)
        if cur < t and cur <= T:
            # can leave
            ans = max(cnt, ans)
            # try easy problems as much as possible
            tmp = (t - 1 - cur) // a
            tmp = min(tmp, easy)
            ans = max(ans, cnt + tmp)

        # force this one
        cnt += 1
        cur += score[d]
        if d == 0:
            easy -= 1
    if cur <= T:
        ans = max(cnt, ans)

    print(ans)
