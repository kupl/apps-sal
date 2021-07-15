n, a = [int(next_token) for next_token in input().split()]
d = [int(next_token) for next_token in input().split()]
s = sum(d)
ans = []
for i in range(n):
    k_min = max(a - s + d[i], 1)
    k_max = min(a - n + 1, d[i])
    ans.append(k_min - 1 + d[i] - k_max)
print(' '.join(map(str, ans)))
