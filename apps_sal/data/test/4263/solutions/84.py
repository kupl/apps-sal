S = input()

N = len(S)
ans = 0
for i in range(N):
    for j in range(i, N):
        T = list(S[i:j + 1])
        M = len(T)

        flag = True
        for k in range(M):
            if T[k] != 'A' and T[k] != 'C' and T[k] != 'G' and T[k] != 'T':
                flag = False
                break
        if flag:
            ans = max(ans, M)

print(ans)
