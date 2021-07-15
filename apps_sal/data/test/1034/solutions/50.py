import sys
import heapq

X, Y, Z , K = map(int, sys.stdin.readline().split())
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
B = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
C = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

ans_heapq = []
i = 0
j = 0
k = 0
heapq.heappush(ans_heapq, [-1 * (A[0] + B[0] + C[0]), i, j, k])
ijk_list = [[0, 0, 0]]
            
for _ in range(K):
    ans, i, j, k = heapq.heappop(ans_heapq)
    print(-1 * ans)
    if i < X - 1 and [i + 1, j, k] not in ijk_list:
        abc = -1 * (A[i + 1] + B[j] + C[k])
        heapq.heappush(ans_heapq, [abc, i + 1, j, k])
        ijk_list.append([i + 1, j, k])
    if j < Y - 1 and [i, j + 1, k] not in ijk_list:
        abc = -1 * (A[i] + B[j + 1] + C[k])
        heapq.heappush(ans_heapq, [abc, i, j + 1, k])
        ijk_list.append([i, j + 1, k])
    if k < Z - 1 and [i, j, k + 1] not in ijk_list:
        abc = -1 * (A[i] + B[j] + C[k + 1])
        heapq.heappush(ans_heapq, [abc, i, j, k + 1])
        ijk_list.append([i, j, k + 1])
