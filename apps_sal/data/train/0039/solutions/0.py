t = int(input())
for tt in range(t):
    (a, b, p) = map(int, input().split())
    s = input()
    n = len(s)
    cost = [0] * n
    cost[-1] = 0
    typ = ''
    i = n - 2
    while i >= 0:
        if s[i] == typ:
            cost[i] = cost[i + 1]
        else:
            typ = s[i]
            cost[i] = cost[i + 1] + (a if typ == 'A' else b)
        i -= 1
    i = 0
    while cost[i] > p:
        i += 1
    print(i + 1)
