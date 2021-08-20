S = input()
K = int(input())
ans = 1
for i in range(len(S)):
    if int(S[i]) > 1 and i < K:
        ans = int(S[i])
        break
print(ans)
