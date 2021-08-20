S = input()
T = input()
ans = 100000
for i in range(len(S) - len(T) + 1):
    score = 0
    U = S[i:i + len(T)]
    for j in range(len(T)):
        if U[j] != T[j]:
            score += 1
    ans = min(ans, score)
print(ans)
