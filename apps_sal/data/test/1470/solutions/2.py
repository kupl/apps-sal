x = int(input())
if x <= 11:
    if x <= 6:
        print(1)
    else:
        print(2)
else:
    ans = x // 11 * 2
    x = x % 11
    if x == 0:
        print(ans)
    elif x <= 6:
        print(ans + 1)
    else:
        print(ans + 2)
