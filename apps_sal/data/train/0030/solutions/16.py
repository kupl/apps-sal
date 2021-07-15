for irjfr in range(int(input())):
    input()
    s = input()
    res = int(s[0] == s[-1] == '1')
    for i in range(len(s) - 1):
        res += int(s[i] == s[i + 1] == '1')
    print(res)
