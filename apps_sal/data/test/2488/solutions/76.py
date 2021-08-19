from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def solve():

    def makeBIT(numEle):
        numPow2 = 2 ** (numEle - 1).bit_length()
        data = [0] * (numPow2 + 1)
        return (data, numPow2)

    def setInit(As):
        for (iB, A) in enumerate(As, 1):
            data[iB] = A
        for iB in range(1, numPow2):
            i = iB + (iB & -iB)
            data[iB] -= data[i]

    def addValue(iA, A):
        iB = iA + 1
        while iB > 0:
            data[iB] += A
            iB -= iB & -iB

    def getValue(iA):
        iB = iA + 1
        ans = 0
        while iB <= numPow2:
            ans += data[iB]
            iB += iB & -iB
        return ans
    (N, D, A) = list(map(int, input().split()))
    XHs = [tuple(map(int, input().split())) for _ in range(N)]
    XHs.sort()
    (Xs, Hs) = ([], [])
    for (X, H) in XHs:
        Xs.append(X)
        Hs.append(H)
    (data, numPow2) = makeBIT(N)
    setInit(Hs)
    ans = 0
    for i in range(N):
        rest = getValue(i)
        if rest <= 0:
            continue
        pos = Xs[i] + D
        iR = bisect_right(Xs, pos + D) - 1
        num = -(-rest // A)
        ans += num
        damage = num * A
        addValue(iR, -damage)
    print(ans)


solve()
