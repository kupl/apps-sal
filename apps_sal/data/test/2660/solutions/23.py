from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

Q = int(input())
ss = input()
t, A, B = list(map(int, ss.split()))
PQ1, PQ2 = [-A], [A]
fr = to = A
minF = 0
accB = B
anss = []
for _ in range(Q-1):
    ss = input()
    if ss[0] == '1':
        t, A, B = list(map(int, ss.split()))
        if fr <= A <= to:
            heappush(PQ1, -A)
            heappush(PQ2, A)
        elif A < fr:
            p = -heappop(PQ1)
            heappush(PQ2, p)
            heappush(PQ1, -A)
            heappush(PQ1, -A)
            minF += fr-A
        else:
            p = heappop(PQ2)
            heappush(PQ1, -p)
            heappush(PQ2, A)
            heappush(PQ2, A)
            minF += A-to
        fr = -heappop(PQ1)
        to = heappop(PQ2)
        heappush(PQ1, -fr)
        heappush(PQ2, to)
        accB += B
    else:
        anss.append((fr, minF+accB))

print(('\n'.join([str(x[0])+' '+str(x[1]) for x in anss])))

