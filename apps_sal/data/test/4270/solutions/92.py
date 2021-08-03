N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = A[0]
for i in range(1, N):
    ans = (ans + A[i]) / 2
print(ans)
