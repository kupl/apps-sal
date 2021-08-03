def inpl(): return list(map(int, input().split()))


N = int(input())
A = inpl()
B = [0]
for a in A:
    if B[-1] != a:
        B.append(a)

B = B[1:]
k = len(B)
dp = [0] * ((k * k + k) // 2)
for d in range(1, k):
    for i in range(k - d):
        if B[i] == B[i + d]:
            dp[d * (2 * k - d + 1) // 2 + i] = dp[(d - 2) * (2 * k - d + 3) // 2 + i + 1] + 1
        else:
            dp[d * (2 * k - d + 1) // 2 + i] = 1 + min(dp[(d - 1) * (2 * k - d + 2) // 2 + i], dp[(d - 1) * (2 * k - d + 2) // 2 + i + 1])
print(dp[-1])
