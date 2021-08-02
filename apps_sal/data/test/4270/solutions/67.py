N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
ans = 0
a = 1
for i in range(N):
    if i != N - 1:
        a *= 0.5
    ans += a * A[i]

print(ans)
