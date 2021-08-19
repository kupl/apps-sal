import bisect
n = int(input())
p = list(map(int, input().split()))
idx = [0] * (n + 1)
for (i, p_i) in enumerate(p):
    idx[p_i] = i
right_idx = list(range(1, n + 1)) + [n, n]
left_idx = list(range(-1, n - 1)) + [-1, -1]
ans = 0
for p in range(1, n + 1):
    x = idx[p]
    r1 = right_idx[x]
    r2 = right_idx[r1]
    l1 = left_idx[x]
    l2 = left_idx[l1]
    ans += p * ((x - l1) * (r2 - r1) + (l1 - l2) * (r1 - x))
    right_idx[l1] = r1
    left_idx[r1] = l1
print(ans)
