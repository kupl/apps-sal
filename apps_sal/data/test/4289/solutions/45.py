n = int(input())
(t, a) = list(map(int, input().split()))
h = list(map(int, input().split()))
ts = [abs(t - x * 0.006 - a) for x in h]
now = ts[0]
ans = 1
for i in range(n):
    if ts[i] < now:
        ans = i + 1
        now = ts[i]
print(ans)
