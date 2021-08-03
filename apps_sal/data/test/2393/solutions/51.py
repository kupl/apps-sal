t = int(input())
for g in range(0, t):
    s = input()
    i = 0
    n = len(s)
    ans = []
    while i < n - 2:
        if s[i:i + 3] == "two":
            if s[i + 2:i + 5] == "one":
                ans += [i + 2 + 1]
                i += 5
            else:
                ans += [i + 1 + 1]
                i += 3
        elif s[i:i + 3] == "one":
            ans += [i + 1 + 1]
            i += 3
        else:
            i += 1
    print(len(ans))
    print(*ans)
