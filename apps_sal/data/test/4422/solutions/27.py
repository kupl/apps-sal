(N, K) = map(int, input().split())
S = input()
ans = ''
for i in range(N):
    if i == K - 1:
        if S[i] == 'A':
            ans += 'a'
        elif S[i] == 'B':
            ans += 'b'
        else:
            ans += 'c'
    else:
        ans += S[i]
print(ans)
