import heapq as hp
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

q1 = []
for i in range(N):
    hp.heappush(q1, A[i])

Psum = [0]*(N+1)
Psum[0] = sum(q1)

for i in range(N):
    a1 = hp.heappop(q1)
    p = max(a1, A[N+i])
    hp.heappush(q1, p)
    Psum[i+1] = Psum[i] + p - a1

q2 = []
for i in range(N):
    hp.heappush(q2, -A[i+2*N])

Qsum = [0]*(N+1)
Qsum[N] = sum(q2)

for i in range(N-1, -1, -1):
    a2 = hp.heappop(q2)
    p = max(a2, -A[N+i])
    hp.heappush(q2, p)
    Qsum[i] = Qsum[i+1] + p - a2


for i in range(N+1):
    if i == 0:
        ans = Psum[i]+Qsum[i]
    ans = max(Psum[i]+Qsum[i], ans)
print(ans)
