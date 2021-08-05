n, k = list(map(int, input().split()))
if n // 2 < k:
    k = n - k
i = 1
count = 1
ans = [1]
for _ in range(n):
    i += k
    if i > n + 1:
        count += 1
        ans.append(ans[-1] + count)
        count += 1
        i -= n
    else:
        ans.append(ans[-1] + count)
print(*ans[1:])
