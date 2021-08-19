(n, x) = list(map(int, input().split()))
l = list(map(int, input().split()))
b = [0] * n
f = [0] * n
pref = [0] * n
pref[0] = l[0]
for i in range(1, n):
    pref[i] = pref[i - 1] + l[i]
b[0] = x * l[0]
mini = 0
for i in range(1, n):
    mini = min(mini, pref[i - 1])
    b[i] = x * l[i] + max(b[i - 1], pref[i - 1] - mini)
f[n - 1] = l[n - 1] * x
maksi = pref[n - 1]
for i in range(1, n):
    j = n - i - 1
    maksi = max(maksi, pref[j])
    f[j] = x * l[j] + max(f[j + 1], maksi - pref[j])
wyn = -100000000000000000000000
for i in range(n):
    wyn = max(wyn, f[i] + b[i] - x * l[i])
mini = 0
wyn1 = -100000000000000000000000
for i in range(n):
    mini = min(mini, pref[i])
    wyn1 = max(wyn1, pref[i] - mini)
print(max(wyn, wyn1))
