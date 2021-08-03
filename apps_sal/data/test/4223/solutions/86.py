N = int(input())
S = input()
ans = 1
for i in range(N - 1):
    if S[i + 1] != S[i]:
        ans += 1
print(ans)
