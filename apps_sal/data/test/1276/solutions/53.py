N = int(input())
S = input()
ans = S.count("R") * S.count("G") * S.count("B")

for i in range(N):
    for j in range(i + 1, N):
        k = 2 * j - i
        if k < N and S[i] != S[j] != S[k] != S[i]:
            ans -= 1

print(ans)
