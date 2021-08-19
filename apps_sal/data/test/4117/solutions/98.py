N = int(input())
L = list(map(int, input().split()))
Ls = sorted(L)
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if Ls[i] < Ls[j] < Ls[k] and Ls[k] < Ls[i] + Ls[j]:
                ans += 1
print(ans)
