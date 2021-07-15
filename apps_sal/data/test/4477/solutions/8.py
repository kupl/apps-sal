for __ in range(int(input())):
    n = input()
    ans = (int(n[0]) - 1) * 10 + 1
    if len(n) >= 2:
        ans += 2
    if len(n) >= 3:
        ans += 3
    if len(n) >= 4:
        ans += 4
    print(ans)
