from heapq import heappop, heappush
t = 1
for test in range(t):
    n = int(input())
    D = {}
    for i in range(1, n + 1):
        a, b = list(map(int, input().split()))
        D[i] = [a, b]

    if n == 3:
        ans = (1, 2, 3)
    else:
        ans = [1]
        a, b = D[1]
        if a in D[b]:
            ans.append(b)
            ans.append(a)
        else:
            ans.append(a)
            ans.append(b)

        while len(ans) < n:
            a, b = D[ans[-2]]
            if ans[-1] == a:
                ans.append(b)
            else:
                ans.append(a)
    print(*ans)
