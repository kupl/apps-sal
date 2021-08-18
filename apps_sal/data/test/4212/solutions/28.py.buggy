# C - Many Requirements
# 再帰関数(n重のfor文)
N, M, Q = map(int, input().split())
abcd = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    abcd.append((a, b, c, d))
max_score = 0


def dfs(A):
    nonlocal max_score
    if len(A) == N:
        # 処理
        score = 0
        for ai, bi, ci, di in abcd:
            if A[bi - 1] - A[ai - 1] == ci:
                score += di
        return score
    # 一つ前の値を保持
    if len(A) >= 1:
        prev_last = A[-1]
    else:
        prev_last = 1
    # 1つ前の値より大きい値の範囲
    for i in range(prev_last, M + 1):
        A.append(i)
        max_score = max(max_score, dfs(A))
        A.pop()
    return max_score  # ループの途中のdfs (len(A) != N のとき) に値を返す


dfs([])
print(max_score)
