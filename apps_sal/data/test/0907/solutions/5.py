t = 1
for test in range(t):
    ans = 'NO'
    (n, m) = list(map(int, input().split()))
    arr = []
    for i in range(m):
        (a, b) = list(map(int, input().split()))
        tmp = [a, b]
        arr.append(tmp)
    x = arr[0][0]
    y = [i for i in range(n + 1)]
    y = set(y)
    for pair in arr:
        if x not in pair:
            y = y.intersection(set(pair))
    if len(y) > 0:
        ans = 'YES'
    x = arr[0][1]
    y = [i for i in range(n + 1)]
    y = set(y)
    for pair in arr:
        if x not in pair:
            y = y.intersection(set(pair))
    if len(y) > 0:
        ans = 'YES'
    print(ans)
