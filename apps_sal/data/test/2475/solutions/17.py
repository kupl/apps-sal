N = int(input())
S = list(map(int, input().split()))
ans = 0
for d in range(1, N):
    max_now = 0
    if (N - 1) % d == 0:
        now = 0
        (i, j) = (0, N - 1)
        while i < j:
            now += S[i] + S[j]
            max_now = max(now, max_now)
            i += d
            j -= d
    else:
        now = 0
        (i, j) = (0, N - 1)
        while i < N - 1 and j > d:
            now += S[i] + S[j]
            max_now = max(now, max_now)
            i += d
            j -= d
    ans = max(max_now, ans)
print(ans)
