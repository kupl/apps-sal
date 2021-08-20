N = int(input())
A = list(map(int, input().split()))
ans = 0
A.sort()
for i in range(N):
    ans += abs(A[i] - (i + 1))
print(ans)
