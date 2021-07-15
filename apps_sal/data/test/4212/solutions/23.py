#!/usr/bin/env python3
# スペース区切りの整数の入力

def dfs(seq):
    ans = 0
    if len(seq) == N:
        score_ret = 0
        for a, b, c, d in data:
            if seq[b-1] - seq[a-1] == c:
                score_ret += d
        return score_ret
    else:
        for i in range(seq[-1], M+1):
            seq_next = seq + (i,)
            score = dfs(seq_next)
            ans = max(ans, score)
    
    return ans

# スペース区切りの整数の入力
N, M, Q = list(map(int, input().split()))
#配列の入力
data = [list(map(int, input().split())) for _ in range(Q)]

ans = -1
score = dfs((1,))
ans = max(ans, score)
print(ans)

