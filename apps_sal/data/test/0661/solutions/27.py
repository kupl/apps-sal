(m, k) = map(int, input().split())
if k > 2 ** m - 1:
    print(-1)
elif k == 0:
    ans = [i for i in range(2 ** m)]
    ans = ans + ans[::-1]
    print(*ans)
elif m == 1:
    print(-1)
else:
    ans = []
    for i in range(2 ** m):
        if i == k:
            continue
        ans.append(i)
    ans = [k] + ans + [k] + ans[::-1]
    print(*ans)
