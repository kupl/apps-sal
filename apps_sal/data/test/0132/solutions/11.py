n = int(input())
a = [int(i) for i in input().split()]
a = a + a
pref_sum = [0] * (2 * n)
for i in range(2 * n):
    pref_sum[i] = pref_sum[i - 1] + a[i]
dif = int(1000000000.0)
for i in range(n):
    for j in range(n):
        dif = min(dif, abs(pref_sum[n - 1] - 2 * (pref_sum[j + i] - pref_sum[j])))
print(dif)
