N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] = A[i] // 2
        ans += 1
print(ans)
