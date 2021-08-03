import heapq
import sys
X, Y, A, B, C = list(map(int, input().split()))
Av = list(map(int, input().split()))
Bv = list(map(int, input().split()))
Cv = list(map(int, input().split()))
heapq.heapify(Av)
heapq.heapify(Bv)
heapq.heapify(Cv)
for i in range(A - X):
    heapq.heappop(Av)
for i in range(B - Y):
    heapq.heappop(Bv)
if C > X + Y:
    for i in range(C - (X + Y)):
        heapq.heappop(Cv)
    NotTake = X + Y
else:
    NotTake = C
total = X + Y
C = NotTake
for _ in range(NotTake):
    Amin = heapq.heappop(Av)
    Bmin = heapq.heappop(Bv)
    Cmin = heapq.heappop(Cv)
    if X > 0 and Amin == min(Amin, Bmin, Cmin):
        heapq.heappush(Bv, Bmin)
        heapq.heappush(Cv, Cmin)
        X -= 1
    elif Y > 0 and Bmin == min(Bmin, Cmin):
        heapq.heappush(Av, Amin)
        heapq.heappush(Cv, Cmin)
        Y -= 1
    elif C > 0:
        heapq.heappush(Av, Amin)
        heapq.heappush(Bv, Bmin)
        C -= 1
    if X == 0 or Y == 0 or C == 0:
        break
NotTake = X + Y + C - total
if X == 0:
    Iv = Bv
    Jv = Cv
    I = Y
    J = C
elif Y == 0:
    Iv = Av
    Jv = Cv
    I = X
    J = C
else:
    print((sum(Av) + sum(Bv) + sum(Cv)))
    return

for _ in range(NotTake):
    Imin = heapq.heappop(Iv)
    Jmin = heapq.heappop(Jv)
    if I > 0 and Imin == min(Imin, Jmin):
        heapq.heappush(Jv, Jmin)
        I -= 1
    elif J > 0:
        heapq.heappush(Iv, Imin)
        J -= 1
    if J == 0 or I == 0:
        break

print((sum(Av) + sum(Bv) + sum(Cv)))
