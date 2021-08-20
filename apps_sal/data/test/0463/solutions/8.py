t = 1
for test in range(1, t + 1):
    (n, x) = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = set(b)
    ans = -1
    if len(a) - len(b) < 0:
        ans = 0
    else:
        D = {}
        for i in b:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        for i in b:
            if i & x in D:
                if i == i & x:
                    if D[i] > 1:
                        ans = 1
                        break
                else:
                    ans = 1
                    break
        if ans == -1:
            tmp = []
            for i in b:
                tmp.append(i & x)
            if len(tmp) > len(set(tmp)):
                ans = 2
    print(ans)
