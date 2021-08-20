(n, m) = list(map(int, input().split()))
neibs_count = [0 for _ in range(n + 1)]
max_len = [0 for _ in range(n + 1)]
prevs = [[] for _ in range(n + 1)]
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    prevs[max(a, b)].append(min(a, b))
    neibs_count[a] += 1
    neibs_count[b] += 1
max_ans = 0
for i in range(1, n + 1):
    max_prev_len = 0
    for prev in prevs[i]:
        max_prev_len = max(max_prev_len, max_len[prev])
    max_len[i] = max_prev_len + 1
    max_ans = max(max_ans, max_len[i] * neibs_count[i])
print(max_ans)
