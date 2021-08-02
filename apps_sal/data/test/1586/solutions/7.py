N = int(input())
if N % 2 == 1:
    print(0)
else:
    ans = 0
    judge = 10
    while True:
        if judge > N:
            break
        else:
            ans += N // judge
            judge *= 5
    print(ans)
