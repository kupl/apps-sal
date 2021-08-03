from itertools import accumulate as acc

H, W, K = list(map(int, input().split()))
S = [list(map(int, list(input()))) for _ in range(H)]

acc_list = [list(acc([0] + s)) for s in S]


def solve(l, x, limit):
    part_num = len(l) - 1
    ok, ng = x, W + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        score = 0
        for i in range(part_num):
            s = 0
            for j in range(l[i], l[i + 1]):
                # print(i, j, mid)
                s += acc_list[j][mid] - acc_list[j][x]
            score = max(s, score)
        if score <= limit:
            ok = mid
        else:
            ng = mid
    return ok


min_num = 10**18
for i in range(1 << (H - 1)):
    l = []
    for j in range(H - 1):
        if (i >> j) & 1:
            l.append(j + 1)
    h_split_num = len(l)
    l = [0] + l + [H]
    x = solve(l, 0, K)
    w_split_num = 0
    flag = True
    while x < W:
        w_split_num += 1
        r = solve(l, x, K)
        if x == r:
            flag = False
            break
        x = r
    if flag:
        split_num = w_split_num + h_split_num
        min_num = min(split_num, min_num)

print(min_num)
