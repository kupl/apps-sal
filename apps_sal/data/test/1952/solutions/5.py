n, k = list(map(int, input().split()))
ms = sorted(list(map(int, input().split())))
cs = list(map(int, input().split()))

d = [0] * (k + 1)
for m in ms:
    d[m] += 1

sums = [0] * (k + 1)
sums[k] = d[k]
for i in range(k - 1, 0, -1):
    sums[i] = sums[i + 1] + d[i]

sums = sums[1:]
ans = -1
for i in range(k):
    ans = max(ans, (sums[i] + cs[i] - 1) // cs[i])

print(ans)
for i in range(ans):
    res = [str(ms[j]) for j in range(n - 1 - i, -1, -ans)]
    print(len(res), end=" ")
    print(" ".join(res))

