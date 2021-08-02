n, k = map(int, input().split())
if k > n or (k == 1 and n > 1):
    print(-1)
    return
if n == 1:
    print('a')
else:
    d = n - k + 2
    ans = 'ab' * (d // 2) + 'a' * (d % 2)
    ind = 2
    for i in range(d, n):
        ans += chr(ord('a') + ind)
        ind += 1
    print(ans)
