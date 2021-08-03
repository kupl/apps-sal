n = int(input())
a = list(map(int, input().split()))
asum = [0] * (n + 1)

for i in range(n):
    asum[i + 1] = asum[i] + a[i]

ans = 10**12
for i in range(1, n):
    snu = asum[i]
    arai = asum[-1] - asum[i]
    ans_ = abs(snu - arai)
    if ans > ans_:
        ans = ans_

print(ans)
