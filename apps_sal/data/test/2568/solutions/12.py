for nt in range(int(input())):
    s = input()
    n = len(s)
    cur = 0
    loop = 0
    ans = 0
    for i in range(n):
        if s[i] == '+':
            cur += 1
        else:
            cur -= 1
        if cur + loop < 0:
            ans += i + 1
            loop += 1
    print(ans + n)
