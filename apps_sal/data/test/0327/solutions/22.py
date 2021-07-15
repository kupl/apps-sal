n, k = list(map(int, input().split()))

if k == 1:
    ans = n
else:
    ans = 1
    while ans <= n:
        ans *= 2
    ans -= 1
print(ans)

