(n, k) = map(int, input().split())
a = list(map(int, input().split()))
pref = [0 for i in range(n - k + 1)]
pref[0] = sum(a[:k])
for i in range(1, n - k + 1):
    pref[i] = pref[i - 1] - a[i - 1] + a[i + k - 1]
print(sum(pref) / (n - k + 1))
