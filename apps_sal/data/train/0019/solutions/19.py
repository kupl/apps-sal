t = int(input())
for i in range(t):
    n, k, d = map(int, input().split())
    data = list(map(int, input().split()))
    
    dd = {}
    for j in range(d):
        elem = data[j]
        if elem in dd:
            dd[elem] += 1
        else:
            dd[elem] = 1
    m = len(dd)
    for j in range(d, n):
        elem = data[j]
        if elem in dd:
            dd[elem] += 1
        else:
            dd[elem] = 1
        dd[data[j - d]] -= 1
        if dd[data[j - d]] == 0:
            dd.pop(data[j - d])
        m = min(m, len(dd))
    print(m)
