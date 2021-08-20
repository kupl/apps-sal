(n, k) = [int(i) for i in input().split()]
if k == 1:
    print(n)
else:
    ans = 1
    while ans <= n:
        ans *= 2
    ans -= 1
    print(ans)
