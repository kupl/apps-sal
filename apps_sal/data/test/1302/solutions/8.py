(n, k) = list(map(int, input().split()))
if k == n:
    print(-1)
else:
    ans = [i for i in range(1, k + 2)]
    for i in range(k + 2, 2 * n // 2, 2):
        ans.append(i + 1)
        ans.append(i)
    if (n + k) % 2 == 0 and k < n - 1:
        ans[0] = n
        ans.append(1)
    print(*ans)
