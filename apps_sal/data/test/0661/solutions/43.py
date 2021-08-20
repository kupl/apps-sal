(m, k) = map(int, input().split())
if k > 2 ** m - 1:
    print(-1)
elif m == 1 and k == 1:
    print(-1)
else:
    (a, b) = (0, 0)
    i = 0
    while k > 0:
        if k % 2:
            a += 2 ** i
        k //= 2
        i += 1
    if a == 0:
        ans = []
        for i in range(2 ** m):
            ans.append(i)
            ans.append(i)
    else:
        ans = [0] * 2 ** (m + 1)
        ans[2 ** m - 1] = b
        ans[-1] = a
        ans[2 ** m] = a
        ans[0] = b
        s = {a, b}
        idx = 0
        for i in range(2 ** m):
            if i not in s:
                ans[idx + 1] = i
                ans[-2 - idx] = i
                idx += 1
    print(*ans)
