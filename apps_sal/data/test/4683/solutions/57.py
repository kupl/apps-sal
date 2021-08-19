N = int(input())
A = list(map(int, input().split()))
rsum = [0 for _ in range(N)]
ans = 0
for i in range(N):
    if i == 0:
        continue
    rsum[-(i + 1)] = rsum[-i] + A[-i]
for i in range(N):
    ans += A[i] * rsum[i]
ans %= 10 ** 9 + 7
print(ans)
