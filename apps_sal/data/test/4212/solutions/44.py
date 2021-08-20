from collections import deque


def calc(seq):
    score = 0
    for (a, b, c, d) in array:
        if seq[b - 1] - seq[a - 1] == c:
            score += d
    return score


(N, M, Q) = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
que = deque()
for i in range(1, M + 1):
    que.append([i])
while que:
    seq = que.popleft()
    if len(seq) == N:
        score = calc(seq)
        ans = max(ans, score)
    else:
        for i in range(seq[-1], M + 1):
            seq_next = seq + [i]
            que.append(seq_next)
print(ans)
