t = int(input())
for k in range(t):
    n = int(input())
    ans = 0
    while n > 0:
        ans += n
        n >>= 1
    print(ans)
