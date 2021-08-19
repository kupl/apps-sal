N, M = map(int, input().split())
stu = []
for v in range(N):
    ai, bi = map(int, input().split())
    stu.append((v, ai, bi))
cp = []
for w in range(M):
    ci, di = map(int, input().split())
    cp.append((w, ci, di))
# 大きい番号から調べることで同じ値のとき最小のチェックポイントに行ける
cp = cp[::-1]
ans = [0] * N
# ある学生について
for i, x, y in stu:
    # あるチェックポイントについて
    mindist = 10**16
    cp_num = 0
    for j, k, l in cp:
        dist = abs(x - k) + abs(y - l)
        if mindist >= dist:
            mindist = dist
            cp_num = j + 1
    ans[i] = cp_num
for n in ans:
    print(n)
