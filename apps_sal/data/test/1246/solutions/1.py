from heapq import *

n = int(input())
heap = []
ops = []
for i in range(n):
    ln = input().rstrip()
    if ln[0] == 'i':
        X = int(ln.split()[1])
        heappush(heap, X)
        ops.append(ln)
        continue
    if ln[0] == 'g':
        X = int(ln.split()[1])
        while heap and heap[0] < X:
            heappop(heap)
            ops.append("removeMin")
        if not heap or heap[0] > X:
            ops.append("insert " + str(X))
            heappush(heap, X)
        ops.append(ln)
        continue

    if not heap:
        ops.append("insert 1")
    else:
        heappop(heap)
    ops.append(ln)
print(len(ops))
print("\n".join(ops))
