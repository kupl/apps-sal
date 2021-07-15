# 入力
N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1

# スコア計算
def score(A):
    tmp = 0
    for ai, bi, ci, di in zip(a, b, c, d):
        if A[bi] - A[ai] == ci:
            tmp += di
    return tmp

# DFS
def dfs(A):
    if len(A) == N:
        return score(A) # 数列 A のスコアを返す
    res = 0
    prev_last = A[-1] if len(A) > 0 else 0
    for v in range(prev_last, M):
        A.append(v)
        res = max(res, dfs(A)) # 再帰呼出しながら、スコア最大値も更新
        A.pop()
    return res

# 求める
print(dfs([]))
