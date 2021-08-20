(n, k) = map(int, input().split())
a = [int(i) for i in input().split()]
a = [0] + a + [0]
i = 1
tot = 0
j = 1
cnt = [0] * (k + 1)
while i <= n:
    while j <= n and a[j] == a[i]:
        j += 1
    tot += 1
    if a[i - 1] == a[j]:
        cnt[a[i]] += 2
    else:
        cnt[a[i]] += 1
    i = j
tot -= 1
ans = tot
for i in range(1, k + 1):
    if ans > tot - cnt[i]:
        ans = tot - cnt[i]
        res = i
print(res)
