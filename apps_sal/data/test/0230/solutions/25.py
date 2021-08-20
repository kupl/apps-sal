N = int(input())
S = str(input())
ans = 0
j = 0
for i in range(N):
    while j < N and S[i:j] in S[j:]:
        ans = max(ans, j - i)
        j += 1
print(ans)
