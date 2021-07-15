from math import gcd


N, *A = list(map(int, open(0).read().split()))

acc_l = [0] * (N + 1)
acc_r = [0] * (N + 1)
for i in range(1, N + 1):
    acc_l[i] = gcd(acc_l[i - 1], A[i - 1])
    acc_r[i] = gcd(acc_r[i - 1], A[-i])
ans = 0
for i in range(N + 1):
    ans = max(ans, gcd(acc_l[i], acc_r[N - i - 1]))
print(ans)

