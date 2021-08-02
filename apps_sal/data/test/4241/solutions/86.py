S = input()
T = input()

ans = 1000
for i in range((len(S) - len(T) + 1)):
    ans_sub = 0
    for j in range(len(T)):
        if T[j] != S[i + j]:
            ans_sub += 1
    ans = min(ans, ans_sub)

print(ans)
