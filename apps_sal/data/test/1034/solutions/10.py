import heapq as hq
x, y, z, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
abc = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]
used = set((0, 0, 0))
while K > 0:
    K -= 1
    p, i, j, k = hq.heappop(abc)
    print((-p))
    for a, b, c in [(i + 1, j, k), (i, j + 1, k), (i, j, k + 1)]:
        if a < x and b < y and c < z and (a, b, c) not in used:
            used.add((a, b, c))
            hq.heappush(abc, (-(A[a] + B[b] + C[c]), a, b, c))
