inf = float('inf')

N = int(input())
a = tuple(map(int, input().split()))

c_sum = [0]
t = 0
for aa in a:
    t += aa
    c_sum.append(t)

ans = inf
p, q = 0, 2  # c_sum上のindex
for cut in range(2, N - 2 + 1):
    # [0, cut)と[cut, N)に分ける
    # 各区間を二分割する
    # 分割位置は、要素の合計の差が最小になるように取る

    # c_sum上のカーソルpを動かす
    # 右区間に一つ以上の要素が含まれるように、pはcut-1まで取る
    # c_sum[p]: 二分割した左区間の和
    # c_sum[cut] - c_sum[p]: 二分割した右区間の和
    while p < cut - 1:
        if abs(c_sum[cut] - c_sum[p] * 2) >= abs(c_sum[cut] - c_sum[p + 1] * 2):
            p += 1
        else:
            break

    # c_sum上のカーソルqを動かす
    # 右区間に一つ以上の要素が含まれるように、qはN-1まで取る
    # c_sum[q]: 二分割した左区間の和
    # c_sum[N] - c_sum[q]: 二分割した右区間の和
    while q < N - 1:
        if abs(c_sum[N] - c_sum[q] - (c_sum[q] - c_sum[cut])) >= abs(
                c_sum[N] - c_sum[q + 1] - (c_sum[q + 1] - c_sum[cut])):
            q += 1
        else:
            break

    cands = [c_sum[cut] - c_sum[p], c_sum[p], c_sum[N] - c_sum[q], c_sum[q] - c_sum[cut]]
    # print(cands)
    ans = min(ans, max(cands) - min(cands))
print(ans)

