N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(N):
        if i == j: continue
        ans = max(ans, abs(A[i] - A[j]))

print(ans)
