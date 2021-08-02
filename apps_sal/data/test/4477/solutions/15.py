for _ in range(int(input())):
    s = input()
    ans = 10 * (int(s[0]) - 1)
    l = len(s)
    if l == 1:
        ans += 1
    elif l == 2:
        ans += 3
    elif l == 3:
        ans += 6
    else:
        ans += 10
    print(ans)
