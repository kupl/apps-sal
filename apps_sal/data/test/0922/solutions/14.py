(n, a) = map(int, input().split())
d = list(map(int, input().split()))
s = sum(d)
ans = []
for i in range(n):
    k_min = max(a - s + d[i], 1)
    k_max = min(a - n + 1, d[i])
    ans.append(k_min - 1 + d[i] - k_max)
print(' '.join(map(str, ans)))
