for _ in range(int(input())):
    s = input()
    n = len(s)
    s = [int(s[i]) for i in range(n)]
    ans = 2
    for a in range(10):
        for b in range(10):
            temp = 0
            sign = 'a'
            for i in range(n):
                if sign == 'a':
                    if s[i] == a:
                        temp += 1
                        sign = 'b'
                elif s[i] == b:
                    temp += 1
                    sign = 'a'
            if a == b:
                ans = max(ans, temp)
            else:
                temp -= temp % 2
                ans = max(ans, temp)
    print(n - ans)
