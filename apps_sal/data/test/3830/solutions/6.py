t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    a = s.count('>')
    b = s.count('<')
    if a == 0 or b == 0:
        print(n)
    else:
        s = s[-1] + s
        ans = 0
        for i in range(1, n + 1):
            if s[i] == '-' or s[i - 1] == '-':
                ans += 1
        print(ans)
