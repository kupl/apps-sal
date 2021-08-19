N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(1, len(A)):
    height = max(0, A[i - 1] - A[i])
    A[i] += height
    ans += height
print(ans)
