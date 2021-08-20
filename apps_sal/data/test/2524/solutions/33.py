N = int(input())
A = list(map(int, input().split()))
M = 10 ** 9 + 7
ans = 0
for n in range(61):
    ones = sum([1 for a in A if a >> n & 1])
    ans += (1 << n) * ones * (N - ones)
    ans %= M
print(ans)
