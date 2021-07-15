N, K = map(int,input().split())
S = input()
ans = []
for i in range(N):
    if i == K - 1:
        x = ord(S[i])
        x += 32
        y = chr(x)
        ans.append(y)
    else:
        ans.append(S[i])

print(''.join(ans))
