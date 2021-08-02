N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    tmp = min(A[i], B[i])
    ans += tmp
    tmp = min(A[i + 1], B[i] - tmp)
    A[i + 1] -= tmp
    ans += tmp
print(ans)
