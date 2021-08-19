#N = int(input())
S = str(input())
#X, Y = map(int, input().split())
#C = list(map(int, input().split()))
N = len(S)
ans = N
for i in range(1, N):
    if S[i] != S[i - 1]:
        now = max(i, N - i)
        ans = min(ans, now)

print(ans)
