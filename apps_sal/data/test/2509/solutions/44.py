n, k = map(int, input().split())

if k == 0:
    print(n * n)
    return

ans = 0
for i in range(k+1, n+1):
    quo, rem = divmod(n, i)
    ans += quo * (i-k)
    if rem >= k:
        ans += rem - k + 1

print(ans)
