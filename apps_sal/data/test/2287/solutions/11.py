for i in range(int(input())):
    s = input()
    k = -1
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            if k == -1:
                k = i
            else:
                ans += i - k - 1
                k = i
    print(ans)
