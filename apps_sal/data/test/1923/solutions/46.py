N = int(input())
A = list(map(int, input().split()))
A2 = sorted(A, reverse=True)
ans = 0
for n in range(N):
    ans += A2[2 * n + 1]
print(ans)
