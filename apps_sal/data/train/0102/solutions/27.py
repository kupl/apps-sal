for i in range(int(input())):
    n = int(input())
    s = len(str(n)) - 1
    ans = s * 9
    if n >= int(str(n)[0] * (s + 1)):
        ans += int(str(n)[0])
    else:
        ans += int(str(n)[0]) - 1
    print(ans)

