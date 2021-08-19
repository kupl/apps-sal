def check(data):
    n = len(data)
    s = sorted(zip(data, range(n)))
    m = s[0][0][1]
    left = set()
    for (i, r) in enumerate(s):
        left.add(r[1])
        if i == len(s) - 1:
            return '-1'
        m = max(m, r[0][1])
        if s[i + 1][0][0] > m:
            break
    res = ['1' if j in left else '2' for j in range(n)]
    return ' '.join(res)


T = int(input())
for i in range(T):
    n = int(input())
    data = []
    for j in range(n):
        (l, r) = map(int, input().split())
        data.append((l, r))
    print(check(data))
