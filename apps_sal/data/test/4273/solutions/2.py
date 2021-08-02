N = int(input())
S = [input()[0] for _ in range(N)]
A = [S.count(c) for c in "MARCH"]
ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += A[i] * A[j] * A[k]
print(ans)
