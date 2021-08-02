N = int(input())
if N % 2 == 1:
    print(0)
else:
    ans = 0
    tmp = N // (5 * 2)
    i = 1
    while tmp > 0:
        ans += tmp
        i += 1
        tmp = N // (2 * 5**i)
    print(ans)
