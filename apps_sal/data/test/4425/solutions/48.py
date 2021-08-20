(N, K) = map(int, input().split())
ans = 0
for i in range(N):
    x = i + 1
    ave = 1 / N
    while x < K:
        x *= 2
        ave /= 2
    ans += ave
print(ans)
