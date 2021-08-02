K = int(input())
N = 50
n = K // N
ans = [49 + n] * N
K %= N

for i in range(N):
    if i < K:
        ans[i] += N - K + 1
    else:
        ans[i] -= K

print(N)
print(*ans)
