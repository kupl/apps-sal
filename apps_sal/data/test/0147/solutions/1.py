import sys
import heapq
# sys.stdin=open("data.txt")
input = sys.stdin.readline

n, a, b = map(int, input().split())

if a < b:
    a, b = b, a

if b == 0:
    # 1 01 001 0001 ... is optimal, plus a long series of 0's
    print((n - 1) * a)
else:
    # pascal's triangle thing
    pascal = [[1] * 20005]
    for i in range(20004):
        newrow = [1]
        for j in range(1, 20005):
            newrow.append(newrow[-1] + pascal[-1][j])
            if newrow[-1] > n:
                break
        pascal.append(newrow)

    def getcom(a, b):
        # return a+b choose b
        # if larger than n, return infinite
        if len(pascal[a]) > b:
            return pascal[a][b]
        if b == 0:
            return 1
        if b == 1:
            return a
        return 100000005

    # start with the null node (prefix cost 0)
    # can split a node into two other nodes with added cost c+a+b
    # new nodes have prefix costs c+a, c+b
    # want n-1 splits in total
    remain = n - 1
    ans = 0
    possible = [[a + b, 1]]    # [c,count]
    while 1:
        # cost u, v leaves
        u, v = heapq.heappop(possible)
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
