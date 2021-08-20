from collections import Counter
from scipy.sparse.csgraph import floyd_warshall
(H, W) = list(map(int, input().split()))
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]
num_counter = Counter()
for i in range(H):
    num_counter += Counter(A[i])
if -1 in num_counter:
    del num_counter[-1]
if 1 in num_counter:
    del num_counter[1]
nei_graph = floyd_warshall(C, directed=True)
ans = 0
for (k, v) in list(num_counter.items()):
    ans += nei_graph[k][1] * v
print(int(ans))
