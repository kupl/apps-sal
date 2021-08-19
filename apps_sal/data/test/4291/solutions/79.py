(N, Q) = map(int, input().split())
S = input()
cnt = [0] * (N + 1)
for i in range(1, N):
    if S[i - 1] == 'A' and S[i] == 'C':
        cnt[i + 1] = cnt[i] + 1
    else:
        cnt[i + 1] = cnt[i]
for i in range(Q):
    (L, R) = map(int, input().split())
    print(cnt[R] - cnt[L])
