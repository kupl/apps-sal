for _ in range(int(input())):
    (a, b, p) = map(int, input().split())
    s = input()
    d = {'A': a, 'B': b}
    c = '0'
    inv = []
    start = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            inv.append((start, i, s[i - 1]))
            start = i
        elif i == len(s) - 1:
            inv.append((start, i, s[i]))
    (ans, cost) = (len(s) - 1, 0)
    for q in inv[::-1]:
        cost += d[q[2]]
        if cost > p:
            break
        else:
            ans = q[0]
    print(ans + 1)
