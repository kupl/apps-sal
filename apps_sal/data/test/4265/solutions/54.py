S = input()
T = input()
l = len(S)
ans = 0

for i in range(l):
    if S[i] != T[i]:
        ans += 1

print(ans)
