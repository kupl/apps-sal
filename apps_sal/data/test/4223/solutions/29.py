N = int(input())
S = str(input())
i = 0
ans = len(S)
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        ans -= 1
print(ans)
