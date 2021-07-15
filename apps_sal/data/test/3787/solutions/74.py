import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
if A + B - 1 > N:
    print(-1)
    return

a = []
b = []
while N > 0:
    if A == 0 or B == 0:
        print(-1)
        return
    if B >= N:
        b = list(range(N, 0, -1)) + b
        N = 0
    else:
        b = list(range(N, N-B, -1)) + b
        N -= B
        if A - 1 >= N:
            a += list(range(1, N+1))
            N = 0
        else:
            a += list(range(N-A+2, N+1))
            N -= A - 1
    A -= 1
    B -= 1
ans = a + b
print(*ans)
