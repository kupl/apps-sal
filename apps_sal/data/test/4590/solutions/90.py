(n, m, k) = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] += a[i - 1]
for i in range(1, m + 1):
    b[i] += b[i - 1]
ans = 0
b_cnt = m
for a_cnt in range(n + 1):
    if a[a_cnt] > k:
        continue
    while a[a_cnt] + b[b_cnt] > k:
        b_cnt -= 1
    ans = max(ans, a_cnt + b_cnt)
print(ans)
