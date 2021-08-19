for i in range(int(input())):
    x = int(input())
    ans = 0
    ans += 9 * (len(str(x)) - 1)
    ans += int(str(x)[0]) - 1
    if int(str(x)[0] * len(str(x))) <= x:
        ans += 1
    print(ans)
