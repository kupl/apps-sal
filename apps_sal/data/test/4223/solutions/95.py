N = int(input())
S = input()
ans = 1

for n in range(1, N):
    if S[n - 1] != S[n]:
        ans += 1

print(ans)
