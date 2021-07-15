import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0]
for a in A:
    S += [S[-1] + a]

ans = float("inf")
l = 0
r = 2
for i in range(1, N - 1):
    while S[l] < S[i] - S[l + 1]:
        l += 1
    while S[r] - S[i] < S[N] - S[r + 1]:
        r += 1

    a = S[l]
    b = S[i] - S[l]
    c = S[r] - S[i]
    d = S[N] - S[r]

    ans = min(ans, max(a, b, c, d) - min(a, b, c, d))
print(ans)
