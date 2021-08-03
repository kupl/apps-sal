n, k = map(int, input().split())
p = list(map(lambda x: (int(x) + 1) / 2, input().split()))

t = sum(p[:k])
ans = t
for i in range(k, n):
    t += p[i] - p[i - k]
    if ans < t:
        ans = t
print(ans)
