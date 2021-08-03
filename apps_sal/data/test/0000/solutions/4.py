s = input()

sb, eb, sc, ec = -1, -1, -1, -1

for i in range(len(s)):
    if s[i] == '[' and sb == -1:
        sb = i
    elif s[i] == ']':
        eb = i
    elif s[i] == ':' and sc == -1 and sb != -1:
        sc = i

if eb <= sb or sc > eb:
    print(-1)
elif sb == -1 or eb == -1 or sc == -1:
    print(-1)
else:
    for i in range(sc + 1, eb):
        if s[i] == ':':
            ec = i
    if ec == -1:
        print(-1)
    else:
        cnt = 0
        for i in range(sc, ec):
            if (s[i] == '|'):
                cnt += 1
        print(cnt + 4)
