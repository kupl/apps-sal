N, X, M = map(int, input().split())

A = [-1, X]
pre = X
sums = [-1, X]
presum = X

for _ in range(M + 1):
    pre = (pre * pre) % M
    A.append(pre)

    presum += pre
    sums.append(presum)

if N <= M:
    print(sums[N])
    return

lstart = M + 1

while A[lstart] != pre:
    lstart -= 1

loopsum = sums[-1] - sums[lstart]

looplen = M + 2 - lstart
loopcnt = (N - lstart) // looplen
over = (N - lstart) % looplen

ans = loopsum * loopcnt + sums[lstart + over]

print(ans)
