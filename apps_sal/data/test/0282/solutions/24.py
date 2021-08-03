def solve():
    n, d = list(map(int, input().split()))
    n -= 1
    s = input()

    i = 0
    res = 0
    while (i < len(s)):
        r = min(len(s) - 1, i + d)
        for j in range(r, i, -1):
            if (s[j] == '1'):
                i = j
                res += 1
                break
        else:
            print(-1)
            return
        if (i == n):
            print(res)
            return


solve()
