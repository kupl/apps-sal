n, k, q = list(map(int, input().split()))
friends = list(map(int, input().split()))
main = [None] * k
for i in range(q):
    t, p = list(map(int, input().split()))
    if t == 1:
        for j in range(k):
            if main[k - j - 1] == None:
                main[k - j - 1] = p - 1
                break
            elif friends[main[k - j - 1]] < friends[p - 1]:
                nn = p - 1
                for l in range(k - j):
                    nnn = main[k - j - l - 1]
                    main[k - j - l - 1] = nn
                    nn = nnn
                break
    elif t == 2:
        if p - 1 in main:
            print("YES")
        else:
            print("NO")
