(m, k) = map(int, input().split())
if pow(2, m) <= k:
    print(-1)
elif not m == 1:
    ans = [k] * pow(2, m + 1)
    i = 0
    for j in range(pow(2, m) - 1):
        if i == k:
            i += 1
        ans[j] = i
        ans[pow(2, m + 1) - 2 - j] = i
        i += 1
    print(*ans)
elif k == 0:
    print(0, 0, 1, 1)
else:
    print(-1)
