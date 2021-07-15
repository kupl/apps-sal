S = list(input())
T = list(input())

ans = 0

for i in range(len(S)):
    if S[i] != T[i]:
        ans += 1

print(ans)
