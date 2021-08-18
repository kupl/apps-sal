for _ in range(1):
    n = int(input())
    arr = list(map(int, input().split()))
    d = dict()
    lst = -1
    ans = 0
    bal = 0
    d[0] = -1
    for i in range(n):
        nbal = bal + arr[i]
        if nbal in d:
            k = d[nbal]
            if k >= lst:
                ans += 1
                lst = i - 1
        bal = nbal
        d[bal] = i
    print(ans)
