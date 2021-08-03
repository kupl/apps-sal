from itertools import combinations_with_replacement as comb_rplc
N, M, Q = list(map(int, input().split()))
array = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
for seq in comb_rplc(list(range(1, M + 1)), N):
    score = 0
    for a, b, c, d in array:
        if seq[b - 1] - seq[a - 1] == c:
            score += d
    ans = max(score, ans)
print(ans)
