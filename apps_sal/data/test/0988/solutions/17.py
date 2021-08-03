def f(x, y):
    return 3 - y + (x == 1)


def g(y):
    return y // 2


S = list()
ans = 0
for i in range(0, 6):
    s = input()
    for j in range(0, len(s)):
        if (s[j] == '.'):
            ans = max(ans, f(j // 3, g(i)))
    S.append(s)
flag = True
for i in range(0, 6):
    s = S[i]
    if flag:
        for j in range(0, len(s)):
            if (s[j] == '.' and f(j // 3, g(i)) == ans):
                if (j == 0):
                    s = 'P' + s[1:]
                else:
                    s = s[0:j] + 'P' + s[(j + 1):]
                flag = False
                break
    print(s)
