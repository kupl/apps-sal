def prog():
    s = input()
    ab = []
    mod = 10 ** 9 + 7
    ans = 1
    cnt = 1
    for i in s:
        if i == 'a':
            cnt += 1
        elif i == 'b':
            ans = ans * cnt % mod
            cnt = 1
    ans = ans * cnt % mod
    ans -= 1
    while ans < 0:
        ans += mod
    return ans % mod


print(prog())
