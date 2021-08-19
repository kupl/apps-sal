N = int(input())
S = sorted([input() for _ in range(N)])
ans = 1
for i in range(N - 1):
    if S[i] != S[i + 1]:
        ans += 1
print(ans)
