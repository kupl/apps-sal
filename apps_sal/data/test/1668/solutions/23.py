t = int(input())
for ij in range(0, t):
    n = int(input())
    l = []
    ans = 0
    la = []
    li = []
    for i in range(0, n):
        s = input()
        la.append(s)
        if s in l:
            ans += 1
            li.append(i)
        else:
            l.append(s)
    print(ans)
    for i in li:
        s = la[i]
        for k in range(0, 4):
            t = 0
            for j in range(0, 10):
                s1 = s[:k] + str(j) + s[k + 1:]
                if s1 not in l:
                    l.append(s1)
                    la[i] = s1
                    t = 1
                    break
            if t == 1:
                break
    for i in la:
        print(i)
