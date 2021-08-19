(N, Q) = map(int, input().split())
S = input()
LR = [tuple(map(int, input().split())) for _ in range(Q)]
cum = [0] * (N + 1)
cnt = 0
for i in range(1, N):
    if S[i - 1] == 'A' and S[i] == 'C':
        cnt += 1
    cum[i] = cnt
ans = []
for (l, r) in LR:
    result = cum[r - 1] - cum[l - 1]
    ans.append(result)
print(*ans, sep='\n')
