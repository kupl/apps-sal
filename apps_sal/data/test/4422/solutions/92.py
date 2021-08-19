(N, K) = list(map(int, input().split()))
S = input()
ans = ''
for i in range(len(S)):
    if i == K - 1:
        ans += S[i].lower()
    else:
        ans += S[i]
print(ans)
