def LI():
    return list(map(int, input().split()))


N, K = LI()
ans = 0
for i in range(1, N + 1):
    x = 1
    count = i
    while count < K:
        count *= 2
        x /= 2
    ans += x / N
print(ans)
