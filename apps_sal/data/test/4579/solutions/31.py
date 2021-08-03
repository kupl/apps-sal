N = int(input())
S = []
for i in range(N):
    S.append(str(input()))

S.sort()
ans = 1
for i in range(N - 1):
    if S[i] != S[i + 1]:
        ans += 1

print(ans)
