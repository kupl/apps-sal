t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    m = min(w)
    M = max(w)
    ans = 0
    for i in range(m*2, M*2+1):
        d = dict()
        tmp = 0
        for x in w:
            if i - x in d and d[i-x] > 0:
                d[i-x] -= 1
                tmp += 1
            else:
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
        if ans < tmp:
            ans = tmp
        # print(tmp, i)
    print(ans)

