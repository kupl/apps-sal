(n, k) = map(int, input().split())
a = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
pref_sum = [0] * n
pref_score = [0] * n
for i in range(n):
    pref_sum[i] = pref_sum[i - 1] + a[i]
    pref_score[i] = pref_score[i - 1] + a[i] * t[i]
ans = pref_sum[k - 1] + pref_score[n - 1] - pref_score[k - 1]
for i in range(k, n):
    ans = max(ans, pref_score[i - k] + pref_score[n - 1] - pref_score[i] + pref_sum[i] - pref_sum[i - k])
print(ans)
