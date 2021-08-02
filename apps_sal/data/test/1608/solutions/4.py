MOD = int(1e9) + 7

N = int(input())
A = list(map(int, input().split()))

pow2 = [pow(2, i, MOD) for i in range(N + 1)]

maxa = max(A)
mcnt = [0 for i in range(maxa + 1)]
mans = [0 for i in range(maxa + 1)]
for i in range(N):
    mcnt[A[i]] += 1
for i in range(1, maxa + 1):
    for j in range(i + i, maxa + 1, i):
        mcnt[i] += mcnt[j]
    mans[i] = pow2[mcnt[i]] - 1
for i in range(maxa, 0, -1):
    for j in range(i + i, maxa + 1, i):
        mans[i] = (mans[i] - mans[j]) % MOD
print(mans[1] + (mans[1] < 0) * MOD)
