t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if '<' not in s:
        print(n)
    elif '>' not in s:
        print(n)
    else:
        ans = 0
        for i in range(n):
            if s[i - 1] == '-' or s[i] == '-':
                ans += 1
        print(ans)
