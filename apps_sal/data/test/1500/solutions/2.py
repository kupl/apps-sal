(n, k) = map(int, input().split())
x = list(map(int, input().split()))
ans = 1
tmp = k
for i in range(n - 1):
    if x[i + 1] - x[i] > k:
        print(-1)
        raise SystemExit
    if tmp >= x[i + 1] - x[i]:
        tmp -= x[i + 1] - x[i]
    else:
        ans += 1
        tmp = k - x[i + 1] + x[i]
print(ans)
