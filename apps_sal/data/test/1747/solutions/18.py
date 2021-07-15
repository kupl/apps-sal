n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
cur_r = 0
d = {}
cur_ans = 0
ans_1 = 0
ans_2 = 0

for cur_l in range(n):
    t = a[cur_l]
    d[t] = d.get(t, 0)+1
    if d[t] == 1:
        cur_ans += 1

    while cur_ans > k:
        t = a[cur_r]
        d[t] -= 1
        if not(d[t]):
            cur_ans -= 1
        cur_r += 1

    if cur_l-cur_r+1 > ans:
        ans = cur_l-cur_r+1
        ans_1 = cur_r
        ans_2 = cur_l

print(ans_1+1, ans_2+1)

