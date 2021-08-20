import sys
import heapq
input = sys.stdin.readline
(n, a, b) = map(int, input().split())
if a < b:
    (a, b) = (b, a)
if b == 0:
    print((n - 1) * a)
else:
    pascal = [[1] * 20005]
    for i in range(20004):
        newrow = [1]
        for j in range(1, 20005):
            newrow.append(newrow[-1] + pascal[-1][j])
            if newrow[-1] > n:
                break
        pascal.append(newrow)

    def getcom(a, b):
        if len(pascal[a]) > b:
            return pascal[a][b]
        if b == 0:
            return 1
        if b == 1:
            return a
        return 100000005
    remain = n - 1
    ans = 0
    possible = [[a + b, 1]]
    while 1:
        (u, v) = heapq.heappop(possible)
        while possible and possible[0][0] == u:
            v += possible[0][1]
            heapq.heappop(possible)
        if remain <= v:
            ans += u * remain
            break
        ans += u * v
        remain -= v
        heapq.heappush(possible, [u + a, v])
        heapq.heappush(possible, [u + b, v])
    print(ans)
