t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    period = [0 for i in range(n + 1)]
    first = [-1 for i in range(n + 1)]
    last = [-1 for i in range(n + 1)]
    for i in range(1, len(a)):
        b = a[i]
        if first[b] == -1:
            first[b] = i
            last[b] = i
        else:
            period[b] = max(period[b], i - last[b])
            last[b] = i

    for i in range(1, len(period)):
        period[i] = max(period[i], n - last[i] + 1)

    period = period[1:]
    l = sorted(list(e if e[0] > first[e[1]] else (first[e[1]], e[1]) for e in zip(period, list(range(1, n + 1))) if e[0] > 0))

    ans = []
    AA = n + 5
    ind = 0
    for i in range(1, n + 1):
        if ind < len(l) and l[ind][0] == i:
            AA = min(AA, l[ind][1])
        ans.append(-1 if AA == n + 5 else AA)
        while ind < len(l) and l[ind][0] == i:
            ind += 1

    print(*ans)
