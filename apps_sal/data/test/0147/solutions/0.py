import sys
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
    n -= 1
    lo = 0
    hi = a * int(n ** 0.5 * 2 + 5)
    while 1:
        mid = (lo + hi) // 2
        c0 = 0
        c1 = 0
        for i in range(mid // a + 1):
            j = (mid - i * a) // b
            if (mid - i * a) % b != 0:
                for k in range(j + 1):
                    c0 += getcom(i, k)
                    if c0 > n:
                        break
            else:
                for k in range(j):
                    c0 += getcom(i, k)
                    if c0 > n:
                        break
                c1 += getcom(i, j)
        if n < c0:
            hi = mid - 1
        elif c0 + c1 < n:
            lo = mid + 1
        else:
            lowcost = 0
            for i in range(mid // a + 1):
                j = (mid - i * a) // b
                if (mid - i * a) % b != 0:
                    for k in range(j + 1):
                        lowcost += getcom(i, k) * (i * a + k * b)
                else:
                    for k in range(j):
                        lowcost += getcom(i, k) * (i * a + k * b)
            temp = lowcost + (n - c0) * mid
            print(temp + n * (a + b))
            break
