(N, K) = map(int, input().split())
S = input()
ans = ''
for i in range(N):
    if i != K - 1:
        ans += S[i]
    else:
        ans += S[i].lower()
print(ans)
