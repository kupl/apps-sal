S = input()
N = len(S)
ans = N * [1]

for n in range(N):
    if S[n] == "R" and S[n + 1] == "R":
        ans[n + 2] += ans[n]
        ans[n] = 0
    m = N - n - 1
    if S[m] == "L" and S[m - 1] == "L":
        ans[m - 2] += ans[m]
        ans[m] = 0

print(*ans)
