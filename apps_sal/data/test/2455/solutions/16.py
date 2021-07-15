t = int(input().strip())
for i in range(t):
    s = input()
    ans = []
    for h in [x for x in range(1, 13) if 12 % x == 0]:
        good = False
        w = 12 // h
        for k in range(w):
            ok = True
            for l in range(h):
                if s[l * w + k] != 'X':
                    ok = False
            if ok:
                good = True
        if good:
            ans.append(str(h) + "x" + str(w))
    print(str(len(ans)) + " " + " ".join(ans))
