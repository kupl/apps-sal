good = input()
pat = input()
n = int(input())
for i in range(n):
    s = input()
    q = True
    sc = 0
    x = 0
    while x < len(pat) and sc < len(s):
        if pat[x] == '*':
            dif = len(s) - len(pat) + 1
            cont = False
            sc -= 1
            for j in range(dif):
                sc += 1
                if s[sc] in good:
                    cont = True
                    break
            if cont:
                q = False
                print("NO")
                break
        elif s[sc] != pat[x]:
            if pat[x] != '?' or s[sc] not in good:
                q = False
                print("NO")
                break
        x += 1
        sc += 1
    if x < len(pat):
        if pat[x] == '*':
            x += 1
    if q:
        if x < len(pat) or sc < len(s):
            q = False
            print("NO")
    if q:
        print("YES")
