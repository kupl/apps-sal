from math import gcd


N, *A = list(map(int, open(0).read().split()))
acc_l = [0]
acc_r = [0]
for i in range(N):
    acc_l.append(gcd(acc_l[-1], A[i]))
    acc_r.append(gcd(acc_r[-1], A[N - i - 1]))

ans = 0
for i in range(N):
    ans = max(ans, gcd(acc_l[i], acc_r[N - i - 1]))
print(ans)

