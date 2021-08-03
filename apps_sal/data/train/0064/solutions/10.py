import sys
def input(): return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N, L = list(map(int, input().split()))
    N += 2
    A = [0] + [int(a) for a in input().split()] + [L]
    x1 = 0
    x2 = N - 1
    t1, t2 = 0, 0
    while x2 - x1 > 1:
        a1 = t1 + (A[x1 + 1] - A[x1]) / (x1 + 1)
        a2 = t2 + (A[x2] - A[x2 - 1]) / (N - x2)
        if a1 < a2:
            t1 = a1
            x1 += 1
        else:
            t2 = a2
            x2 -= 1
    if t1 < t2:
        ans = t2 + ((A[x2] - A[x1]) - (x1 + 1) * (t2 - t1)) / (x1 + 1 + N - x2)
    else:
        ans = t1 + ((A[x2] - A[x1]) - (N - x2) * (t1 - t2)) / (x1 + 1 + N - x2)
    print(ans)
