(N, X, M) = map(int, input().split())
step = [0 for i in range(M)]
sums = [i for i in range(M)]
for i in range(len(step)):
    step[i] = i ** 2 % M
ans = 0
while N:
    if N & 1:
        ans += sums[X]
        X = step[X]
    sums = [sums[i] + sums[step[i]] for i in range(M)]
    step = [step[step[i]] for i in range(M)]
    N >>= 1
print(ans)
