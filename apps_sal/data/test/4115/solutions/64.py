S = input()
N = len(S)
ans = 0
for i in range(N // 2):
    if S[i] != S[N - i - 1]:
        ans += 1
print(ans)
