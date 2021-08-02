# 3 N numbers
import heapq
N = int(input())
a = list(map(int, input().split()))
S = sum(a[:N])
b = a[:N]
heapq.heapify(b)
dpmax = [S for i in range(N + 1)]
# dpmax[x] = 前半　ｘ + N このうちmax N　このわを記録
for i in range(N, 2 * N):
    heapq.heappush(b, a[i])
    d = heapq.heappop(b)
    S += a[i] - d
    dpmax[i - N + 1] = S

c = a[-N:]
for i in range(N):
    c[i] = -c[i]
T = sum(c)
heapq.heapify(c)
dpmin = [-T for i in range(N + 1)]

# dpmin[x]= 後半　x + N このうち　min Nこのわを記録する
for i in range(N, 2 * N):
    heapq.heappush(c, -a[-1 - i])
    d = heapq.heappop(c)
    T += -a[-1 - i] - d
    dpmin[i + 1 - N] = -T

ans = -1000000000000000000000000000000
for i in range(N + 1):
    ans = max(ans, dpmax[i] - dpmin[N - i])
print(ans)
