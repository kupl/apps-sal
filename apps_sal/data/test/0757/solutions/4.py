from bisect import bisect_left
n, m, k = tuple(map(int, input().split()))
a = sorted(map(int, input().split()), reverse=True)
s = [k] + [0] * n
for i in range(n):
    s[i + 1] = s[i] + a[i] - 1
ans = bisect_left(s, m)

print(ans if ans <= n else -1)
