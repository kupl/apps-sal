import bisect


t = int(input())

tmp_ans = [0] * 40
for i in range(40):
    tmp_ans[i] = 3**i
ruiseki = [0] * 41
for i in range(40):
    ruiseki[i + 1] = ruiseki[i] + tmp_ans[i]

for _ in range(t):
    n = int(input())
    ind = bisect.bisect_left(ruiseki, n)
    ans = ruiseki[ind]

    for i in range(ind)[::-1]:
        if ans - tmp_ans[i] >= n:
            ans -= tmp_ans[i]
    print(ans)
