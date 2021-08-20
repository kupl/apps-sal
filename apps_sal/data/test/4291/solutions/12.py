(N, Q) = list(map(int, input().split()))
S = input()
cnt = [0, 0]
for i in range(1, N):
    cnt.append(cnt[-1] + S[i - 1:i + 1].count('AC'))
for _ in range(Q):
    (l, r) = list(map(int, input().split()))
    print(cnt[r] - cnt[l])
