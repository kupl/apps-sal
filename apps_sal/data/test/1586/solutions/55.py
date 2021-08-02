n = int(input())
if n % 2 == 1:
    print(0)
else:
    ans = 0
    tmp = 10
    while True:
        if tmp > n:
            print(ans)
            break
        else:
            ans += n // tmp
            tmp *= 5
