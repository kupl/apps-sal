t = int(input())

for test in range(t):
    n = int(input())
    ans = ['1' for i in range(n)]

    start, end = dict(), dict()
    for i in range(n):
        a, b = list(map(int, input().split()))
        if a in start:
            start[a].append(i + 1)
        else:
            start[a] = [i + 1]

        if (i + 1) in end:
            end[i + 1].append(b)
        else:
            end[i + 1] = [b]

    st_sorted = sorted(list(start.keys()))

    m = 0
    ok = False
    ans_pos = -1
    for pos in range(len(st_sorted) - 1):
        for i in start[st_sorted[pos]]:
            m = max(m, max(end[i]))
        if m < st_sorted[pos + 1]:
            ok = True
            ans_pos = pos
            break
    if ok:
        for i in range(pos + 1, len(st_sorted)):
            for pos in start[st_sorted[i]]:
                ans[pos - 1] = '2'
        print(' '.join(ans))
    else:
        print(-1)

