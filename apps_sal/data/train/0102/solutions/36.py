for i in range(int(input())):
    n = int(input())
    ch = len(str(n))
    ans = 0
    for i in range(ch - 1):
        ans += 9
    for i in range(int('1' * ch), n + 1, int('1' * ch)):
        ans += 1
    print(ans)
