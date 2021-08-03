S = list(input())
N = len(S)
ans = []
for i in range(N):
    if i % 2 == 0:
        ans.append(S[i])
ans = ''.join(ans)
print(ans)
