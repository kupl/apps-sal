s = input()
t = input()
if s == t:
    print(0)
else:
    p = []
    w = []
    n = len(s)
    k = 0
    for i in range(n):
        if s[i] != t[i]:
            if s[i] in w or t[i] in w:
                print(-1)
                k = -1
                break
            if s[i] < t[i]:
                q = s[i] + t[i]
            else:
                q = t[i] + s[i]
            if not q in p:
                for j in range(k):
                    if (s[i] in p[j]) != (t[i] in p[j]):
                        print(-1)
                        k = -1
                        break
                if k > -1:
                    k += 1
                    p.append(q)
                else:
                    break
        else:
            f = True
            for j in range(k):
                if s[i] in p[j]:
                    f = False
            if f:
                w.append(s[i])
            else:
                k = -1
                print(-1)
                break
        if k == -1:
            break
    if k > 0:
        print(k)
        for i in range(k):
            s = p[i]
            print(s[0], s[1])
