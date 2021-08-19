(n, k) = map(int, input().split())
a = []
for i in range(n):
    tmp = input()
    a.append((len(tmp), tmp))
a.sort()
ans = input()
ansmin = 10 ** 18
ansmax = 0
nowt = 0
for i in range(n):
    if i % k == 0 and i != 0:
        nowt += 5
    nowt += 1
    if len(ans) == len(a[i][1]):
        ansmax = nowt
        ansmin = min(ansmin, nowt)
print(ansmin, ansmax)
