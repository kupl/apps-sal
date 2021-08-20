S = str(input())
T = str(input())
Ans = 0
for i in range(0, len(S)):
    if S[i] == T[i]:
        Ans += 1
print(Ans)
