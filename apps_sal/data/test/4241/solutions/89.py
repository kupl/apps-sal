S = input()
T = input()

ans = 10**9
for i in range(len(S) - len(T) + 1):
    tmp = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            tmp += 1

    ans = min(tmp, ans)

print(ans)
