n, k = list(map(int, input().split()))
ans = []
if n % (2 * k + 1) >= k + 1 or n % (2 * k + 1) == 0:
    i = k + 1
    while i <= n:
        ans.append(i)
        i += 2 * k + 1
else:
    i = 1
    while i <= n:
        ans.append(i)
        i += 2 * k + 1
print(len(ans))
print(*ans)
