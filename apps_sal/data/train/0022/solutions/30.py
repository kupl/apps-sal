for i in range(int(input())):
    a, k = map(int, input().split())
    while '0' not in str(a) and k > 1:
        mi = 10
        ma = -1
        for j in range(len(str(a))):
            if int(str(a)[j]) > ma:
                ma = int(str(a)[j])
            if int(str(a)[j]) < mi:
                mi = int(str(a)[j])
        a += ma * mi
        k -= 1
    print(a)
