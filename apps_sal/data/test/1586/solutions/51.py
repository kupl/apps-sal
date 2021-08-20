N = int(input())
if N % 2 == 0:
    tmp = 10
    ans = 0
    while tmp <= N:
        ans += N // tmp
        tmp = 5 * tmp
    print(ans)
else:
    print(0)
