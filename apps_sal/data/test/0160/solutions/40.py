import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = [int(a) for a in input().split()]
    sumA = sum(A)
    D = []
    for i in range(1, sumA + 1):
        if i ** 2 > sumA: break
        if sumA % i == 0:
            D.append(i)
            if i ** 2 != sumA: D.append(sumA // i)
    D.sort(reverse = True)
    for i, d in enumerate(D):
        L = []
        count = 0
        for a in A:
            if a % d > 0: 
                L.append(a % d)
                count += 1
        L.sort()
        if count > 0:
            minus, plus = [0] * count, [0] * count
            minus[0] = L[0]
            plus[count - 1] = d - L[count - 1]
            for i in range(1, count):
                minus[i] = minus[i-1] + L[i]
                plus[count - 1 - i] = plus[count - i] +  d - L[count - 1 - i]
            Op = K + 1
            for i in range(count - 1):
                if abs(minus[i] - plus[i + 1]) % d == 0: Op = min(Op, max(minus[i], plus[i + 1]))
            if Op <= K:
                print(d)
                break
    else: print(1)

    return 0

def __starting_point():
    solve()
__starting_point()
