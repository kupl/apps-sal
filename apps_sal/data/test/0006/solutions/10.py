import sys
input = sys.stdin.readline
T = int(input())
for testcases in range(T):
    (n, x) = list(map(int, input().split()))
    B = [tuple(map(int, input().split())) for i in range(n)]
    B0 = max(B, key=lambda x: x[0] - x[1])
    dam = B0[0] - B0[1]
    BMAX = max(B)[0]
    if dam <= 0 and x > BMAX:
        print(-1)
    elif BMAX >= x:
        print(1)
    else:
        print(1 + max(0, -((x - BMAX) // -dam)))
