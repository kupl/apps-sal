n = int(input())
(t, a) = map(float, input().split())
h = list(map(float, input().split()))
best = 10 ** 5
ans = -1
for i in range(n):
    tt = t - h[i] * 0.006
    best = min(best, abs(tt - a))
    if abs(a - tt) == best:
        ans = i
print(ans + 1)
