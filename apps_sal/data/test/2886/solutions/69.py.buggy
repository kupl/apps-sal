s = input()
n = len(s)

if len(s) == 2:
    if s[0] == s[1]:
        print((1, 2))
    else:
        print((-1, -1))
else:
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            print((i + 1, i + 2))
            return
    for i in range(n - 2):
        if s[i] == s[i + 2]:
            print((i + 1, i + 3))
            return
    print((-1, -1))
