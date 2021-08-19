(n, k) = map(int, input().split())
ans = []
for i in range(1, 2 * n + 1, 2):
    if k > 0:
        ans.append(i + 1)
        ans.append(i)
        k -= 1
    else:
        ans.append(i)
        ans.append(i + 1)
print(*ans)
