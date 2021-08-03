s = input()
n = len(s)
if n % 2 == 0:
    if s[n // 2 - 1] != s[n // 2]:
        print(n // 2)
    else:
        for i in range(2, n // 2 + 1):
            if s[n // 2 - i] != s[n // 2] or s[n // 2 - 1 + i] != s[n // 2]:
                print(n // 2 + i - 1)
                break
        else:
            print(n)
else:
    for i in range(1, n // 2 + 1):
        if s[n // 2 - i] != s[n // 2] or s[n // 2 + i] != s[n // 2]:
            print(n // 2 + i)
            break
    else:
        print(n)
