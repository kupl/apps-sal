A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(2):
    ans += abs(A[i] - A[i + 1])
print(ans)
