import heapq
N = int(input())
A = list(map(int, input().split()))

X = A[:N]
Y = [-i for i in A[2 * N:]]
heapq.heapify(X)
heapq.heapify(Y)
x = sum(X)
y = -sum(Y)
XMA = [0] * (N + 1)
YMI = [0] * (N + 1)
XMA[0] = x
YMI[N] = y
for i in range(N):
    heapq.heappush(X, A[N + i])
    s = heapq.heappop(X)
    x += A[N + i] - s
    XMA[i + 1] = x

    heapq.heappush(Y, -A[2 * N - 1 - i])
    t = -heapq.heappop(Y)
    y += A[2 * N - 1 - i] - t
    YMI[N - i - 1] = y

ANS = [0] * (N + 1)
for i in range(N + 1):
    ANS[i] = XMA[i] - YMI[i]
print(max(ANS))
