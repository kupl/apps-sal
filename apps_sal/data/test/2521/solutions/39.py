from heapq import heappush, heappop
N = int(input())
A = [int(a) for a in input().split()]
dpx = [0] * (N + 1)
dpy = [0] * (N + 1)
dpx[0] = sum(A[:N])
dpy[-1] = sum(A[2 * N:])
X = []
Y = []
for i in range(N):
    heappush(X, A[i])

for i in range(N):
    heappush(Y, -A[3 * N - 1 - i])

for i in range(N):
    a = heappop(X)
    b = A[N + i]
    if b > a:
        heappush(X, b)
        dpx[i + 1] = dpx[i] + b - a
    else:
        heappush(X, a)
        dpx[i + 1] = dpx[i]

    c = -heappop(Y)
    d = A[2 * N - 1 - i]
    if d < c:
        heappush(Y, -d)
        dpy[N - 1 - i] = dpy[N - i] + d - c
    else:
        heappush(Y, -c)
        dpy[N - 1 - i] = dpy[N - i]

ans = -float('inf')
for i in range(N + 1):
    ans = max(ans, dpx[i] - dpy[i])
print(ans)
