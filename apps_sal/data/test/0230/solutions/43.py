N = int(input())
S = input()
ans = 0
j = 0
for i in range(N):
    while j < N and S[i:j] in S[j:]:
        j += 1
    ans = max(ans, j - i - 1)
print(ans)
