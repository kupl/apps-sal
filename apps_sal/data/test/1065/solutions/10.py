n, k, m, d = list(map(int, input().split()))
ans = 0
for i in range(1, d + 1):
    if m < n // (k * i):
        continue
    if n < (k * (i - 1) + 1):
        break
    ans_here = min(n // (k * (i - 1) + 1), m)
    # print(i, ans_here)
    ans = max(ans, ans_here * i)
print(ans)

