n, a, b, c, t = map(int, input().split())
arr = list(map(int, input().split()))
if(b < c):
    ans = 0
    for i in range(n):
        ans += a + (c - b) * (t - arr[i])
    print(ans)
else:
    ans = 0
    for i in range(n):
        ans += a
    print(ans)
