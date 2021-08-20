[v1, v2] = [int(x) for x in input().split()]
[t, d] = [int(x) for x in input().split()]
left = [v1] * t
for i in range(1, t):
    left[i] = left[i - 1] + d
right = [v2] * t
for i in range(t - 2, -1, -1):
    right[i] = right[i + 1] + d
ans = 0
for i in range(t):
    ans += min(left[i], right[i])
print(ans)
