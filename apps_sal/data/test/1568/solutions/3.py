n, a, b, c, t = list(map(int, input().split()))
l = list(map(int, input().split()))
if b >= c:
    print(a*n)
else:
    ans = 0
    for i in l:
        ans += (t - i)*c + a - b*(t-i)
    print(ans)


