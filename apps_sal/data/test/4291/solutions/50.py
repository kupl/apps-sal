(N, Q) = list(map(int, input().split()))
S = input()
lr = [list(map(int, input().split())) for _ in range(Q)]
s = [0] * N
for i in range(1, N):
    s[i] = s[i - 1]
    if S[i - 1] == 'A' and S[i] == 'C':
        s[i] += 1
for (l, r) in lr:
    print(s[r - 1] - s[l - 1])
